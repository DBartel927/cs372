# Write a function that accepts a URL string as input and returns the path portion only (also as a string).

# For example:

# Input                                Output
# ───────────────────────────────────  ───────────────────────────────
# https://example.com/                 /
# https://example.com/foo              /foo
# https://example.com/bar.txt          /bar.txt
# https://example.com/baz/foo/bar.git  /baz/foo/bar.git
# You can write this by hand, or you can use Python built-ins. (Hint: search for python urlparse.)

from urllib.parse import urlparse

url = input("Enter a URL: ")
parsedurl = urlparse(url)

print(parsedurl.path)
