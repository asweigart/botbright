# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · **🇵🇹 Português** · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright é um clone em JavaScript, em um único arquivo, do jogo de quebra-cabeças em Flash *Lightbot*. Programe um robô isométrico para percorrer uma grade 3D de blocos e acender os blocos azuis de objetivo. Arraste blocos de instrução para a memória do robô, pressione **Executar** e veja seu programa rodar.

O jogo todo é um único arquivo HTML (`botbright.html`) com CSS e JavaScript embutidos — sem build, sem dependências externas, sem chamadas de rede. Abra o arquivo em qualquer navegador moderno e jogue. Salve-o no disco rígido e ele continuará funcionando offline para sempre.

Você também pode mudar o esquema de cores e colocar diferentes chapéus no seu robô. Há um editor de níveis embutido, e níveis e chapéus podem ser importados ou exportados no formato JSON.

## Jogar

Basta dar dois cliques no arquivo botbright.html ou abri-lo no seu navegador. O jogo funciona offline.

Versão online: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Como funciona

O robô tem três áreas de memória:

- **Memória principal** — 12 espaços de instrução, executa quando você pressiona Executar
- **Memória F1** — 8 espaços de instrução, uma função chamável
- **Memória F2** — 8 espaços de instrução, uma segunda função chamável

Arraste blocos de instrução da paleta para a memória. Reordene arrastando entre espaços. Arraste um bloco para fora de qualquer espaço para apagá-lo.

| Instrução | O que faz |
|-------------|------------|
| Avançar | Pisa no bloco à frente, se estiver na mesma altura |
| Virar à esquerda | Gira 90° no sentido anti-horário |
| Virar à direita | Gira 90° no sentido horário |
| Pular | Sobe um nível ou desce qualquer número de níveis |
| Iluminar | Alterna o bloco de objetivo sob o robô |
| Chamar F1 / F2 | Empilha essa função na pilha de chamadas (recursão permitida, com limites) |

Um nível é concluído quando todos os blocos de objetivo estão acesos em amarelo.

Programas que rodam demais são interrompidos: no máximo 1000 instruções no total e 100 quadros na pilha de chamadas.

## Controles

**Câmera** — WASD ou setas para deslocar, Q/E ou PageUp/PageDown para girar 90°, +/− ou roda do mouse para zoom. Pressione 0 para redefinir a vista. Arraste o canvas para deslocar, pince para zoom, gire com dois dedos para rotacionar. Mantenha pressionados os botões de câmera na tela para movimento contínuo e suave.

**Largura da barra lateral** — arraste o divisor entre o canvas e a barra lateral.

**Velocidade** — controle deslizante na barra lateral: lento / normal / rápido. Ajustável durante a execução.

## Editor de níveis

Um editor completo acompanha o jogo. Adicione/duplique/exclua níveis, redimensione a grade (1–32 em cada dimensão), pinte alturas de 0 a 9, marque blocos de objetivo, defina a posição e direção iniciais e teste o nível sem sair do editor.

O conjunto completo de níveis é exportado como JSON e importado da mesma forma, para compartilhar níveis ou fazer cópias de segurança.

## Editor de chapéus

O robô pode usar chapéus. Vem com dezenove opções: Nenhum, Cartola, Chapéu de mago, Coroa, Gorro, Boné, Chapéu de cowboy, Chapéu de festa, Chapéu-coco, Auréola, Chifres do diabo, Sombrero, Chapéu de bruxa, Fez, Chifres, Orelhas de coelho, Orelhas de gato, Capacete de mergulho e Capacete viking. Cada chapéu é definido por quatro sprites SVG — um para cada orientação relativa à tela — para que acompanhe a direção do robô em todas as rotações de câmera (a aba do boné, a fivela do chapéu de bruxa, a vigia do capacete de mergulho e as orelhas de coelho/gato se deslocam conforme necessário). Uma pré-visualização ao vivo gira o robô uma vez por segundo para você ver o chapéu por todos os ângulos. Chapéus também são exportados e importados como JSON para designs personalizados.

## Esquemas de cores

Um painel **Cores** na barra lateral do jogo expõe a paleta: cor dos blocos, cor das bordas dos blocos, cor do objetivo, cor do objetivo aceso, fundo e corpo do robô. Você pode usar um tema integrado ou editá-los você mesmo.

## Idiomas

Traduções da interface em 23 idiomas: inglês, espanhol, francês, alemão, italiano, português, russo, chinês, japonês, coreano, hindi, bengali, vietnamita, árabe (com layout da direita para a esquerda), tailandês, tagalo, norueguês, holandês, sueco, turco, suaíli, indonésio e polonês. O idioma padrão segue o `navigator.language` do navegador; o seletor de idioma na tela inicial o substitui durante a sessão. Os nomes e descrições dos níveis embutidos, bem como os nomes dos chapéus embutidos, estão traduzidos para todos os idiomas suportados. O editor de níveis grava apenas no espaço do idioma selecionado quando você edita um nome ou descrição, deixando as outras traduções intactas.

## Modo claro / escuro

Segue o `prefers-color-scheme` do navegador para a interface. Ao escolher o tema **Padrão** no painel de Cores, é aplicada a paleta correspondente ao modo atual do navegador, mantendo-se sincronizada se você alternar de modo. Qualquer outro tema integrado — ou uma paleta personalizada — substitui esse comportamento.

## Créditos

Criado por Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspirado em *Lightbot* de Daniel Yaroslavski.
