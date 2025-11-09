import os
import datetime
import csv
// main change
print("📂 Thư mục hiện tại:", os.getcwd())

def count_keyword_in_log(filename, keyword):
    """Đếm số dòng chứa keyword trong file log."""
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword.lower() in line.lower():
                count += 1
    return count


def list_file_lines(filename):
    """In ra toàn bộ nội dung file."""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())

def list_files_in_folder(folder_path, output_csv):
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Ghi header
        writer.writerow(["Tên", "Loại", "Kích thước (KB)", "Ngày sửa cuối"])

        for name in os.listdir(folder_path):
            full_path = os.path.join(folder_path, name)
            if os.path.isfile(full_path):
                size_kb = os.path.getsize(full_path) / 1024
                mtime = os.path.getmtime(full_path)
                date_modified = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([name, "File", f"{size_kb:.2f}", date_modified])
            elif os.path.isdir(full_path):
                mtime = os.path.getmtime(full_path)
                date_modified = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([name, "Folder", "-", date_modified])

    print(f"✅ Đã xuất danh sách file ra: {output_csv}")


def list_py_files(folder_path):
    """Hiển thị riêng các file .py."""
    print(f"\n🐍 Các file Python (.py) trong thư mục: {folder_path}")
    py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]
    if py_files:
        for name in py_files:
            print("  📄", name)
    else:
        print("  ⚠️ Không tìm thấy file .py nào.")
