import os
import argparse

# to run from CLI: python rename_cli.py --folder C:\Users\nguye\OneDrive\Pictures --prefix john

def rename_images(folder, prefix="img"):
    files = [f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".png"))]
    for i, f in enumerate(files):
        old_path = os.path.join(folder, f)
        new_name = f"{prefix}_{i+1}{os.path.splitext(f)[1]}"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Đã đổi: {f} → {new_name}")

if __name__ == "__main__":

    #folder = input("Nhập đường dẫn thư mục ảnh: ")
    #prefix = input("Nhập tiền tố (prefix): ")
    #rename_images(folder, prefix)
    
    parser = argparse.ArgumentParser(description="Batch rename images")
    parser.add_argument("--folder", required=True, help="Path to image folder")
    parser.add_argument("--prefix", required=True, help="New filename prefix")
    args = parser.parse_args()
    rename_images(args.folder, args.prefix)

    
