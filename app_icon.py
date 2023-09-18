#!/usr/bin/env python3

import argparse
import json
import os
from PIL import Image, ImageOps, ImageFilter, ImageDraw

def resize_image(image_path, output_folder, size, filename):
    img = Image.open(image_path)
    
    if img.mode == 'RGBA':
        img = img.convert("RGB")
    
    img = img.resize((size, size), Image.LANCZOS)
    img.save(os.path.join(output_folder, filename))

def generate_contents_json(sizes):
    
    icons = []
    for size in sizes:
        for scale in [1, 2, 3]:
            icon = {}
            icon["idiom"] = "iphone"
            icon["size"] = f"{size}x{size}"
            icon["filename"] = f"icon_{size}x{size}@{scale}x.png"
            icon["scale"] = f"{scale}x"
            icons.append(icon)

    contents = {
        "images": icons,
        "info": {
            "version": 1,
            "author": "xcode"
        }
    }

    return json.dumps(contents, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate app icons for Android and iOS.")
    parser.add_argument("image_path", help="Path to the 1024x1024 source image.")
    args = parser.parse_args()

    android_mipmap_levels = ["mipmap-ldpi", "mipmap-mdpi", "mipmap-hdpi", "mipmap-xhdpi", "mipmap-xxhdpi", "mipmap-xxxhdpi"]
    android_sizes = [36, 48, 72, 96, 144, 192]  # Corresponding to the mipmap levels

    if not os.path.exists("Android_Icons"):
        os.makedirs("Android_Icons")

    for level, size in zip(android_mipmap_levels, android_sizes):
        folder_path = os.path.join("Android_Icons", level)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        resize_image(args.image_path, folder_path, size, "ic_launcher.png")

    if not os.path.exists("iOS_Icons"):
        os.makedirs("iOS_Icons")

    if not os.path.exists("iOS_Icons/AppIcon.appiconset"):
        os.makedirs("iOS_Icons/AppIcon.appiconset")

    ios_sizes = [29, 58, 87, 60, 120, 180, 76, 152, 167, 1024]

    for size in ios_sizes:
        for scale in [1, 2, 3]:
            filename = f"icon_{size}x{size}@{scale}x.png"
            resize_image(args.image_path, "iOS_Icons/AppIcon.appiconset", size*scale, filename)

    contents_json = generate_contents_json([29, 60, 76])
    with open("iOS_Icons/AppIcon.appiconset/Contents.json", "w") as f:
        f.write(contents_json)
