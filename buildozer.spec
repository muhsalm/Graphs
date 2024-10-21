[app]

# (str) Title of your application
title = Custom Graphs

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,matplotlib

# (list) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (list) Permissions
android.permissions = INTERNET

# (str) Icon of the application
# Uncomment and set your icon path if you have one
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
# Uncomment and set your presplash path if you have one
# presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity
