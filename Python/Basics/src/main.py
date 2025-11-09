// main XXX
from utils.log_helper import count_keyword_in_log, list_file_lines, list_files_in_folder, list_py_files

import os

// main rebase

// main change
// main add
// test change

def main():
    // test rebase
    while True:
        folder = input("Nhập đường dẫn thư mục: ").strip()
        if not os.path.isdir(folder):
            print("❌ Thư mục không tồn tại. Vui lòng kiểm tra lại!")
            continue
    
        print("\n=== MENU ===")
        print("1. Xem tất cả file/thư mục")
        print("2. Lọc file .py")
        print("3. Tìm từ khóa trong file example.log")
        print("4. Thoát")

        choice = input("👉 Nhập lựa chọn (1/2/3/4): ").strip()

        if choice == "1":
            output = "file_list.csv"
            list_files_in_folder(folder, output)
        elif choice == "2":
            list_py_files(folder)
        elif choice == "3":
            filename = "example.log"  # đường dẫn tương đối (ra ngoài 1 cấp)
            keyword = input("Nhập từ khóa cần tìm: ")
            result = count_keyword_in_log(filename, keyword)
            print(f"\nSố dòng chứa '{keyword}' là: {result}\n")
            print("📄 Nội dung file log:")
            list_file_lines(filename)
        elif choice == "4":
            print("👋 Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng nhập lại (1-3).")

if __name__ == "__main__":
    main()
