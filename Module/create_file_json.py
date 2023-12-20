import json

# Dữ liệu bạn muốn lưu vào file JSON
data = {
    "train": [
        {
            "id": "L_01",
            "report": "Gan: Kích thước bình thường, nhu mô đều, có khối u cư trú, hệ thống tĩnh mạch trên gan, tĩnh mạch cửa không giãn, không có huyết khối.",
            "image_path": ["liver_01/0.png", "liver_01/1.png"],
            "split": "train"
        },
        {
            "id": "K_01",
            "report": "Thận: Thận phải kích thước bình thường, nhu mô bình thường, phân biệt tuỷ - vỏ rõ, đài bể thận không giãn, phát hiện hình ảnh sỏi.",
            "image_path": ["kidney_01/0.png", "kidney_01/1.png"],
            "split": "train"
        }
    ]
}

# Tên file JSON bạn muốn tạo
json_file_path = "data/annotation.json"

# Mở file để ghi dữ liệu
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    # Sử dụng hàm dump để ghi dữ liệu vào file JSON
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"File JSON đã được tạo: {json_file_path}")

