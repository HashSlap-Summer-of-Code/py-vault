#!/usr/bin/env python3



import os
import argparse
from PIL import Image

def resize_images(folder_path, width, height):
    supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")

    if not os.path.exists(folder_path):
        print(f"[!] Folder not found: {folder_path}")
        return

    output_dir = os.path.join(folder_path, "resized")
    os.makedirs(output_dir, exist_ok=True)

    count = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_formats):
            image_path = os.path.join(folder_path, filename)
            try:
                with Image.open(image_path) as img:
                    resized_img = img.resize((width, height))
                    resized_img.save(os.path.join(output_dir, filename))
                    count += 1
            except Exception as e:
                print(f"[!] Failed to resize {filename}: {e}")

    print(f"\n Resized {count} images to {width}x{height} and saved to '{output_dir}'")

def main():
    parser = argparse.ArgumentParser(description="Resize all images in a folder.")
    parser.add_argument("folder", help="Path to the image folder")
    parser.add_argument("--width", type=int, required=True, help="Target width in pixels")
    parser.add_argument("--height", type=int, required=True, help="Target height in pixels")
    
    args = parser.parse_args()
    resize_images(args.folder, args.width, args.height)

if __name__ == "__main__":
    main()
