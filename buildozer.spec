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

p4a.local_recipes = ./recipes

# Disable native APIs (needed if generating PDFs or not using JNI)
android.use_android_native_api = False

log_level = 2
