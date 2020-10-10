import os

cwd = r"test"
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))