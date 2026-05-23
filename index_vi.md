# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · [🇫🇷 Français](index_fr.md) · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · **🇻🇳 Tiếng Việt** · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md)

---

Botbright là bản sao JavaScript một tệp duy nhất của trò chơi đố vui Flash *Lightbot*. Lập trình một robot góc nhìn isometric để đi trên lưới ô 3D và thắp sáng các ô đích màu xanh. Kéo các ô lệnh vào bộ nhớ của robot, nhấn **Chạy** và xem chương trình của bạn thực thi.

Toàn bộ trò chơi nằm trong một tệp HTML duy nhất (`botbright.html`) với CSS và JavaScript nội tuyến — không cần build, không phụ thuộc bên ngoài, không gọi mạng. Mở tệp trên bất kỳ trình duyệt hiện đại nào và chơi. Lưu vào ổ cứng và nó sẽ luôn chạy ngoại tuyến mãi mãi.

Bạn cũng có thể đổi bảng màu và đội nhiều loại mũ khác nhau cho robot. Có sẵn trình chỉnh sửa màn, còn các màn và mũ có thể nhập/xuất theo định dạng JSON.

## Chơi

Chỉ cần nhấp đúp vào tệp botbright.html hoặc mở trong trình duyệt. Trò chơi hoạt động ngoại tuyến.

Phiên bản trực tuyến: [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Cách hoạt động

Robot có ba vùng bộ nhớ:

- **Bộ nhớ chính** — 12 ô lệnh, chạy khi bạn nhấn Chạy
- **Bộ nhớ F1** — 8 ô lệnh, một hàm có thể gọi
- **Bộ nhớ F2** — 8 ô lệnh, một hàm có thể gọi thứ hai

Kéo các ô lệnh từ bảng vào bộ nhớ. Đổi thứ tự bằng cách kéo giữa các ô. Kéo một ô ra khỏi ô lệnh để xóa.

| Lệnh | Tác dụng |
|-------------|------------|
| Tiến | Bước lên ô phía trước nếu cùng độ cao |
| Quay trái | Xoay 90° ngược chiều kim đồng hồ |
| Quay phải | Xoay 90° theo chiều kim đồng hồ |
| Nhảy | Nhảy lên một bậc, hoặc nhảy xuống bất kỳ số bậc nào |
| Thắp sáng | Bật/tắt ô đích ngay dưới robot |
| Gọi F1 / F2 | Đẩy hàm đó vào ngăn xếp lời gọi (cho phép đệ quy, có giới hạn) |

Một màn hoàn thành khi mọi ô đích đều sáng vàng.

Chương trình chạy quá lâu sẽ bị dừng: tối đa 1000 lệnh tổng cộng, tối đa 100 khung trong ngăn xếp lời gọi.

## Điều khiển

**Máy quay** — WASD hoặc phím mũi tên để di chuyển, Q/E hoặc PageUp/PageDown để xoay 90°, +/− hoặc cuộn chuột để thu phóng. Nhấn 0 để đặt lại tầm nhìn. Kéo canvas để di chuyển, chụm để thu phóng, vặn bằng hai ngón tay để xoay. Giữ các nút máy quay trên màn hình để di chuyển liên tục mượt mà.

**Chiều rộng thanh bên** — kéo đường phân cách giữa canvas và thanh bên.

**Tốc độ** — thanh trượt trong thanh bên: chậm / bình thường / nhanh. Có thể điều chỉnh khi đang chạy.

## Trình chỉnh sửa màn

Trò chơi đi kèm trình chỉnh sửa đầy đủ. Thêm/nhân đôi/xóa màn, đổi kích thước lưới (1–32 ở mỗi chiều), tô độ cao 0–9, đánh dấu ô đích, đặt vị trí và hướng xuất phát, và thử nghiệm ngay trong trình chỉnh sửa.

Toàn bộ tập màn được xuất ra JSON và nhập cùng cách, để bạn chia sẻ màn hoặc sao lưu chỉnh sửa.

## Trình chỉnh sửa mũ

Robot có thể đội mũ. Mặc định có mười chín lựa chọn: Không có, Mũ chóp cao, Mũ phù thủy, Vương miện, Mũ len, Mũ lưỡi trai, Mũ cao bồi, Mũ tiệc, Mũ quả dưa, Vầng hào quang, Sừng quỷ, Sombrero, Mũ phù thủy, Mũ fez, Gạc nai, Tai thỏ, Tai mèo, Mũ lặn, và Mũ Viking. Mỗi chiếc mũ được định nghĩa bằng bốn sprite SVG — mỗi hướng trên màn hình một sprite — nên mũ luôn đi theo hướng của robot dù máy quay xoay thế nào (lưỡi trai, khóa mũ phù thủy, ô cửa mũ lặn, và phần trong tai thỏ/mèo đều dịch chuyển tương ứng). Bản xem trước trực tiếp xoay robot mỗi giây một lần để bạn xem mũ từ mọi góc. Mũ cũng có thể xuất/nhập dưới dạng JSON cho thiết kế tùy chỉnh.

## Bảng màu

Bảng **Màu** trong thanh bên trò chơi hiển thị bảng màu: màu ô, màu cạnh ô, màu đích, màu đích sáng, nền và thân robot. Bạn có thể dùng chủ đề tích hợp hoặc tự chỉnh sửa.

## Ngôn ngữ

Bản dịch giao diện cho 23 ngôn ngữ: tiếng Anh, Tây Ban Nha, Pháp, Đức, Ý, Bồ Đào Nha, Nga, Trung, Nhật, Hàn, Hindi, Bengali, Việt, Ả Rập (bố cục từ phải sang trái), Thái, Tagalog, Na Uy, Hà Lan, Thụy Điển, Thổ Nhĩ Kỳ, Swahili, Indonesia và Ba Lan. Ngôn ngữ mặc định lấy từ `navigator.language` của trình duyệt; bộ chọn ngôn ngữ trên màn hình bắt đầu sẽ ghi đè trong phiên. Tên và mô tả các màn tích hợp, cùng tên các mũ tích hợp, đều được dịch sang tất cả ngôn ngữ được hỗ trợ. Khi bạn sửa tên hoặc mô tả, trình chỉnh sửa chỉ ghi vào ô của ngôn ngữ hiện đang chọn, giữ nguyên các bản dịch ngôn ngữ khác.

## Chế độ Sáng / Tối

Phần khung ứng dụng theo `prefers-color-scheme` của trình duyệt. Chọn chủ đề **Mặc định** trong bảng Màu sẽ áp dụng bảng màu khớp với chế độ hiện tại của trình duyệt, nên vẫn đồng bộ khi bạn chuyển chế độ. Mọi chủ đề tích hợp khác — hoặc bảng màu tùy chỉnh do bạn chỉnh — sẽ ghi đè hành vi này.

## Ghi công

Tạo bởi Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Lấy cảm hứng từ *Lightbot* của Daniel Yaroslavski.
