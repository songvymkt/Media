# Bản dựng Reel

40 giây, 1080 × 1920, 30 fps; MP4 H.264 với AAC.

Voice: file MiniMax do người dùng cung cấp. Giảm tốc độ còn 0.84× bằng FFmpeg atempo, giữ cao độ, thêm khoảng đệm đầu/cuối để đạt 40 giây. Các cảnh được căn theo đoạn lời đọc thay vì giữ cứng mốc cảnh trong brief ban đầu.

Ảnh minh họa do AI tạo, đã kiểm tra hình nắp kính đóng và chỉnh riêng chi tiết ống xả bị gập / thông thoáng. Không có footage người thật hoặc lip-sync. Tên thương hiệu dùng chữ, không tái tạo logo. Không dùng hình người thợ trong ảnh tham khảo làm nhận diện cá nhân.

Phụ đề lấy nguyên nội dung kịch bản người dùng; mốc cụm câu căn theo khoảng ngắt đo được trong voice. Không có nhận dạng từng từ tự động. File SRT riêng đi kèm video đã chèn phụ đề.

Nhạc nền instrumental nhẹ được tổng hợp riêng trong `build.py`, không dùng bản nhạc thương mại của bên thứ ba.

## Dựng lại

Các asset đã lưu cục bộ trong `assets/`, gồm ảnh, voice đã xử lý, nhạc, GSAP và font Be Vietnam Pro với giấy phép trong `assets/fonts/package/LICENSE`.

Trong thư mục này, chạy:

```sh
XDG_CACHE_HOME=/workspace/.cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm_config_cache=/workspace/.npm-cache npm run check
XDG_CACHE_HOME=/workspace/.cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npm_config_cache=/workspace/.npm-cache npm run render -- --output ../Thinh-Tin-Phat-Reel-40s.mp4 --fps 30 --quality high --workers 2
```

`build.py` tạo lại HTML, SRT và nhạc từ nội dung đã căn thời gian; không cần chạy lại để render. Cắt cảnh trực tiếp là chủ ý theo yêu cầu người dùng. Photo zoom/crop tràn khỏi khung là chủ ý. Cảnh được giữ trong cùng một composition nên lint có cảnh báo tổ chức timeline, không có lỗi runtime hoặc tràn chữ.
