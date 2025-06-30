[app]
android.build_tools_version = 34.0.0
android.api = 30


version = 0.1
title = GroceryApp
package.name = groceryapp
#package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy,plyer,libffi

android.permissions = INTERNET

p4a.local_recipes = ./recipes

android.minapi = 21
android.ndk = 25b




# For PDF generation
android.use_android_native_api = False

# If using camera or sensors in future
# android.features = android.hardware.camera
log_level = 2
