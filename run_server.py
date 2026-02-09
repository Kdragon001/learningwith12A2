#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple HTTP Server for testing
Phục vụ file HTML với Unicode support
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Lấy thư mục hiện tại
PORT = 9000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Thêm headers để hỗ trợ UTF-8
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Log các request"""
        print(f"[{self.log_date_time_string()}] {format % args}")

# Khởi tạo server
try:
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✓ Server đang chạy tại: http://localhost:{PORT}")
        print(f"✓ Thư mục: {os.getcwd()}")
        print(f"✓ Nhấp vào: http://localhost:{PORT}/index_FIXED.html")
        print("\nNhấp Ctrl+C để dừng server")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n✓ Server đã dừng")
    sys.exit(0)
except OSError as e:
    if "Address already in use" in str(e):
        print(f"✗ Lỗi: Port {PORT} đã được sử dụng")
        print(f"  Thử port khác hoặc dừng chương trình đang dùng port này")
    else:
        print(f"✗ Lỗi: {e}")
    sys.exit(1)
