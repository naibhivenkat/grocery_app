[app]
title = GroceryApp
package.name = groceryapp
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy,plyer,libffi

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.build_tools = 34.0.0
android.ndk = 25b

# Disable native APIs (recommended for FPDF)
android.use_android_native_api = False

log_level = 2
