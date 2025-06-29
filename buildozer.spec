[app]
version = 0.1
title = GroceryApp
package.name = groceryapp
#package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

requirements = python3,kivy,plyer
android.permissions = INTERNET


android.minapi = 21
android.ndk = 25b

android.api = 33
android.build_tools = 36.0.0

# For PDF generation
android.use_android_native_api = False

# If using camera or sensors in future
# android.features = android.hardware.camera
log_level = 2
