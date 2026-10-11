[app]
title = Music Tagger
package.name = musictagger
package.domain = org.tagger
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,mutagen
orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

# Let buildozer automatically handle SDK/NDK selection to prevent initialization crashes
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
