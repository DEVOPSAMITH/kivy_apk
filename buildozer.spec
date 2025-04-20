[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.arch = armeabi-v7a,arm64-v8a

# Permissions
android.permissions = INTERNET

# Assets
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Advanced options
android.private_storage = 1
android.allow_backup = 1
android.logcat_filters = *:S python:D

# Include necessary file types
source.include_patterns = *.py,*.kv,*.png,*.jpg,*.atlas

# Remove debug logs for production
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
android.debug = 1
