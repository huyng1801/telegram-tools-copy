import os
from PIL import Image

def change_icon_to_purple(directory):
    """
    Đổi màu tất cả các file PNG trong thư mục hiện tại thành màu tím.
    :param directory: Đường dẫn thư mục chứa file PNG.
    """
    purple_color = (241, 245, 249)  # Màu tím (RGB)
    
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.png'):
            file_path = os.path.join(directory, file_name)
            try:
                # Mở ảnh PNG
                img = Image.open(file_path).convert("RGBA")
                data = img.getdata()
                
                # Đổi từng pixel sang màu tím (giữ nguyên độ trong suốt)
                new_data = [
                    (purple_color[0], purple_color[1], purple_color[2], pixel[3]) if pixel[3] > 0 else pixel
                    for pixel in data
                ]
                img.putdata(new_data)
                
                # Lưu file mới
                new_file_name = f"purple_{file_name}"
                new_file_path = os.path.join(directory, new_file_name)
                img.save(new_file_path)
                print(f"Đã đổi màu: {file_name} -> {new_file_name}")
            except Exception as e:
                print(f"Lỗi khi xử lý file {file_name}: {e}")

# Đổi màu các icon PNG trong thư mục hiện tại thành màu tím
change_icon_to_purple('.')
