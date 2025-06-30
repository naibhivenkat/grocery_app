#title = Grocery App
#package.name = groceryapp
#package.domain = org.test
#source.include_exts = py,png,jpg,kv,atlas,ttf,ttc,otf
#orientation = portrait
#fullscreen = 1
#android.api = 30
#android.build_tools = 34.0.0
#android.minapi = 21
#requirements = python3,kivy,plyer,requests,pillow
#android.permissions = INTERNET
#android.hostpython = 3
#android.ndk = 23b
#android.ndk_path = ~/.buildozer/android/platform/android-ndk-r23b
#android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE


[app]

# (str) Title of your application
title = Grocery App

# (str) Package name
package.name = com.yourcompany.groceryapp

# (str) Package domain (needed for android/ios packaging)
package.domain = yourcompany.com

# (str) Application versioning (method 1)
version = 0.1

# (list) Requirements (aka: dependencies)
requirements = python3,kivy,cffi

# (str) Main application file relative to the source.dir
source.main = main.py

# (str) Directory of the main.py and other source files
source.dir = .

# (str) Kivy version to use
kivy.version = 2.1.0

# (list) Android permissions
android.permissions = INTERNET

# (bool) Indicate if your application should be fullscreen or not
fullscreen = 0


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (if debug mode in buildozer is set))
log_level = 2

# (str) NDK version to use
android.ndk = 25b

# (str) SDK version to use
android.sdk = 30

# (str) AAB or APK. Default is apk
android.release = 0
