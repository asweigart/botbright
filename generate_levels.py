#!/usr/bin/env python3
"""Generate Botbright levels by simulating random programs.

EXPERIMENTAL: This is a rough level generator and the levels it produces are
not of an acceptable quality for the shipped game. It is kept around as a
sketch / starting point — expect awkward layouts, trivial or nonsensical
puzzles, and large variance in difficulty. Treat the output as a source of
ideas to hand-edit rather than as a finished set of levels.

For each level the script picks a random "interesting" program (with optional
F1/F2 functions), then runs it through a Botbright simulator that decides tile
heights and goal positions as the bot moves. The resulting level is guaranteed
to be solved by the generating program (each candidate is sanity-checked by a
second-pass simulator before being kept).

The output JSON matches the Botbright level format used by botbright.html and
adds three solution keys:
  - solution_main: CSV string of the main program
  - solution_f1:   CSV string of the F1 function (empty when unused)
  - solution_f2:   CSV string of the F2 function (empty when unused)
Instruction names are titlecased: Forward, Left, Right, Jump, Light, F1, F2.

Examples:
  python3 generate_levels.py --count 12 --output my-levels.json
  python3 generate_levels.py --count 20 --difficulty hard --seed 42
  python3 generate_levels.py --count 5 --width 10 --height 10

The resulting JSON file can be imported via the in-game level editor.
"""

import argparse
import json
import random
import sys

# 0=N, 1=E, 2=S, 3=W — matches Botbright's coordinate system.
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIR_LETTERS = ['N', 'E', 'S', 'W']

# Botbright execution limits — keep in sync with botbright.html.
MAX_STEPS = 1000
MAX_STACK = 100
MAIN_CAP = 12
F_CAP = 8


def weighted_choice(options):
    """options: list of (item, weight) tuples."""
    total = sum(w for _, w in options)
    r = random.uniform(0, total)
    acc = 0
    for item, w in options:
        acc += w
        if r <= acc:
            return item
    return options[-1][0]


def random_program(length, allow_f1=False, allow_f2=False):
    """Build a random instruction list with movement-heavy bias."""
    opts = [
        ('Forward', 32),
        ('Left', 12),
        ('Right', 12),
        ('Jump', 14),
        ('Light', 18),
    ]
    if allow_f1:
        opts.append(('F1', 14))
    if allow_f2:
        opts.append(('F2', 11))
    return [weighted_choice(opts) for _ in range(length)]


def simulate_build(main, f1, f2, sx, sy, sd, width, height):
    """Simulate the program while building the level.

    Tile heights are decided lazily: the first time the bot tries to step or
    jump onto a tile, we assign that tile a height that makes the move legal.
    Subsequent visits respect the existing decision (so the same instruction
    sequence behaves the same way every time).

    Returns (heights_2d, goals_set, success_bool). `success` is True when the
    program lit at least one goal and ended with every introduced goal still
    lit (i.e. the program is a valid solution to the level it produced).
    """
    grid = {(sx, sy): 0}
    goals = set()
    lit = set()

    bot_x, bot_y = sx, sy
    bot_facing = sd
    bot_h = 0
    moved = False

    programs = {'main': main, 'f1': f1, 'f2': f2}
    call_stack = [('main', 0)]
    steps = 0

    while call_stack and steps < MAX_STEPS:
        prog_name, pc = call_stack[-1]
        prog = programs[prog_name]
        if pc >= len(prog):
            call_stack.pop()
            continue
        call_stack[-1] = (prog_name, pc + 1)
        instr = prog[pc]
        steps += 1

        if instr == 'Forward':
            dx, dy = DIRS[bot_facing]
            nx, ny = bot_x + dx, bot_y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            tgt = grid.get((nx, ny))
            if tgt is None:
                grid[(nx, ny)] = bot_h
                bot_x, bot_y = nx, ny
                moved = True
            elif tgt == bot_h:
                bot_x, bot_y = nx, ny
                moved = True
        elif instr == 'Left':
            bot_facing = (bot_facing + 3) % 4
        elif instr == 'Right':
            bot_facing = (bot_facing + 1) % 4
        elif instr == 'Jump':
            dx, dy = DIRS[bot_facing]
            nx, ny = bot_x + dx, bot_y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            tgt = grid.get((nx, ny))
            if tgt is None:
                # Bias toward jumping up; sometimes pick a lower height.
                if bot_h > 0 and random.random() < 0.35:
                    new_h = random.randint(0, bot_h - 1)
                else:
                    new_h = min(9, bot_h + 1)
                grid[(nx, ny)] = new_h
                bot_x, bot_y = nx, ny
                bot_h = new_h
                moved = True
            else:
                diff = tgt - bot_h
                if diff == 1 or diff < 0:
                    bot_x, bot_y = nx, ny
                    bot_h = tgt
                    moved = True
        elif instr == 'Light':
            here = (bot_x, bot_y)
            if here in lit:
                lit.discard(here)
            else:
                goals.add(here)
                lit.add(here)
        elif instr == 'F1':
            if len(call_stack) < MAX_STACK:
                call_stack.append(('f1', 0))
        elif instr == 'F2':
            if len(call_stack) < MAX_STACK:
                call_stack.append(('f2', 0))

    heights = [[grid.get((x, y), 0) for x in range(width)] for y in range(height)]
    success = bool(goals) and goals == lit and moved
    return heights, goals, success


def simulate_verify(heights, goals_list, sx, sy, sd_letter, width, height,
                    main, f1, f2):
    """Replay the saved solution against the finalized level.

    Mirrors the in-game executor exactly (Forward fails on height mismatch,
    Jump requires +1 or any lower target, Light only toggles real goal tiles).
    Returns True when every goal ends up lit.
    """
    goals = set(tuple(g) for g in goals_list)
    lit = set()
    bot_x, bot_y = sx, sy
    bot_facing = DIR_LETTERS.index(sd_letter)
    bot_h = heights[bot_y][bot_x]

    programs = {'main': main, 'f1': f1, 'f2': f2}
    call_stack = [('main', 0)]
    steps = 0

    while call_stack and steps < MAX_STEPS:
        prog_name, pc = call_stack[-1]
        prog = programs[prog_name]
        if pc >= len(prog):
            call_stack.pop()
            continue
        call_stack[-1] = (prog_name, pc + 1)
        instr = prog[pc]
        steps += 1

        if instr == 'Forward':
            dx, dy = DIRS[bot_facing]
            nx, ny = bot_x + dx, bot_y + dy
            if 0 <= nx < width and 0 <= ny < height and heights[ny][nx] == bot_h:
                bot_x, bot_y = nx, ny
        elif instr == 'Left':
            bot_facing = (bot_facing + 3) % 4
        elif instr == 'Right':
            bot_facing = (bot_facing + 1) % 4
        elif instr == 'Jump':
            dx, dy = DIRS[bot_facing]
            nx, ny = bot_x + dx, bot_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                diff = heights[ny][nx] - bot_h
                if diff == 1 or diff < 0:
                    bot_x, bot_y = nx, ny
                    bot_h = heights[ny][nx]
        elif instr == 'Light':
            here = (bot_x, bot_y)
            if here in goals:
                if here in lit:
                    lit.discard(here)
                else:
                    lit.add(here)
        elif instr == 'F1':
            if len(call_stack) < MAX_STACK:
                call_stack.append(('f1', 0))
        elif instr == 'F2':
            if len(call_stack) < MAX_STACK:
                call_stack.append(('f2', 0))

    return lit == goals


def generate_one(complexity, use_f1, use_f2, width, height, max_attempts=200):
    """Try up to max_attempts random programs; return the first that yields a
    valid puzzle (verified end-to-end). Returns None if nothing worked.
    """
    for _ in range(max_attempts):
        main_len = min(MAIN_CAP, max(2, complexity))
        main = random_program(main_len, use_f1, use_f2)
        f1 = random_program(random.randint(3, F_CAP), use_f1, False) if use_f1 else []
        f2 = random_program(random.randint(3, F_CAP), False, False) if use_f2 else []

        # Pick a starting position with some margin from the grid edges so the
        # program is less likely to butt into a wall early.
        sx = random.randint(width // 4, max(width // 4, 3 * width // 4))
        sy = random.randint(height // 4, max(height // 4, 3 * height // 4))
        sd = random.randint(0, 3)

        heights, goals, ok = simulate_build(main, f1, f2, sx, sy, sd, width, height)
        if not ok or not (1 <= len(goals) <= 16):
            continue

        sd_letter = DIR_LETTERS[sd]
        goals_list = sorted([list(g) for g in goals], key=lambda p: (p[1], p[0]))
        if simulate_verify(heights, goals_list, sx, sy, sd_letter, width, height,
                           main, f1, f2):
            return heights, goals_list, sx, sy, sd_letter, main, f1, f2
    return None


def serialize_map(heights):
    """Heights 2D list -> '\\n'-joined string of single digits."""
    return '\n'.join(''.join(str(min(9, max(0, h))) for h in row) for row in heights)


def main():
    p = argparse.ArgumentParser(
        description='Generate Botbright levels (with bundled solutions).',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument('--count', type=int, default=10,
                   help='Number of levels to generate (default 10)')
    p.add_argument('--output', default='generated-levels.json',
                   help='Output JSON path (default generated-levels.json)')
    p.add_argument('--width', type=int, default=8, help='Level width (default 8)')
    p.add_argument('--height', type=int, default=8, help='Level height (default 8)')
    p.add_argument('--seed', type=int, default=None,
                   help='Random seed (default: time-based)')
    p.add_argument('--difficulty', choices=['easy', 'medium', 'hard', 'mixed'],
                   default='mixed',
                   help='easy = main only, medium = +F1, hard = +F1+F2, '
                        'mixed = ramp easy -> hard across the count (default)')
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    levels = []
    for i in range(args.count):
        if args.difficulty == 'easy':
            d = 0
        elif args.difficulty == 'medium':
            d = 1
        elif args.difficulty == 'hard':
            d = 2
        else:
            t = i / max(1, args.count - 1)
            d = 0 if t < 0.34 else 1 if t < 0.67 else 2

        complexity = [6, 9, 12][d]
        use_f1 = d >= 1
        use_f2 = d >= 2

        result = generate_one(complexity, use_f1, use_f2, args.width, args.height)
        if result is None:
            print(f'[level {i + 1}] generation failed after retries; skipping',
                  file=sys.stderr)
            continue
        heights, goals, sx, sy, sd_letter, main_prog, f1_prog, f2_prog = result
        difficulty_label = ['easy', 'medium', 'hard'][d]
        levels.append({
            'name': f'GENERATED {i + 1}',
            'description': f'Auto-generated ({difficulty_label}, {len(goals)} goal{"s" if len(goals) != 1 else ""}).',
            'width': args.width,
            'height': args.height,
            'start_position': [sx, sy],
            'start_direction': sd_letter,
            'goals': goals,
            'map': serialize_map(heights),
            'solution_main': ','.join(main_prog),
            'solution_f1': ','.join(f1_prog),
            'solution_f2': ','.join(f2_prog),
        })

    with open(args.output, 'w') as f:
        json.dump(levels, f, indent=2)
    print(f'Wrote {len(levels)} level(s) to {args.output}')


if __name__ == '__main__':
    main()
