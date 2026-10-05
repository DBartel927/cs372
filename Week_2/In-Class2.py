# Given a path, return the file extension.

# For example:

# Input                 Output
# ────────────────────  ──────────────
# /                     [empty string]
# /foo                  [empty string]
# /bar.txt              .txt
# /baz/foo/bar.gif      .gif
# /baz/foo/bar.foo.jpg  .jpg
# You can do this manually or use Python built-ins to do it. (Hint: search for python splitext.)

import os

url = input("Enter a URL: ")
root, ext = os.path.splitext(url)
print(ext)

# Given a file extension, return the MIME type.

# For example:

# Input                                Output
# ───────────────────────────────────  ───────────────────────────────
# [empty string]  application/octet-stream [or None]
# .txt            text/plain
# .html           text/html
# .gif            image/gif
# .jpg            image/jpeg
# You can do this manually (in which case you can just support the handful of extensions, above), or you can use Python built-ins. (Hint: search for python mimetypes guess_type.)

import mimetypes

# ext = input("Enter a file extension: ")
mime_type = mimetypes.guess_type(f"file{ext}")[0]
print(mime_type)