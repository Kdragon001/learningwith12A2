#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script doi ten file PDF va cap nhat HTML
"""

import os
import re
from pathlib import Path

# Duong dan toi thu muc chua file PDF
pdf_folder = r"d:\hoc\code\htmml\project1\đề\đề tiếng anh"
html_file = r"d:\hoc\code\htmml\project1\index_FIXED.html"

print("=== Doi Ten File PDF ===")

# Lay danh sach file PDF
pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.endswith('.pdf')])

mappings = {}

# Doi ten cac file
for i, old_name in enumerate(pdf_files, 1):
    old_path = os.path.join(pdf_folder, old_name)
    new_name = f"de_{i:02d}.pdf"  # de_01.pdf, de_02.pdf, ...
    new_path = os.path.join(pdf_folder, new_name)
    
    # Doi ten file
    os.rename(old_path, new_path)
    mappings[old_name] = new_name
    
    print(f"OK {i}. {old_name} -> {new_name}")

print(f"\n=== Cap Nhat Link Trong HTML ===")

# Doc file HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Thay the tung link
for old_name, new_name in mappings.items():
    old_path = f"đề/đề tiếng anh/{old_name}"
    new_path = f"đề/đề tiếng anh/{new_name}"
    
    # Use regex to replace (case-insensitive)
    html_content = html_content.replace(old_path, new_path)
    
    print(f"OK: {old_name} -> {new_name}")

# Ghi lai file HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("\nHoan tat! Tat ca file da duoc doi ten va link da cap nhat.")
