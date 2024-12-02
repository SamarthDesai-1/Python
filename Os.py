import os

directoryPath = "/"

contents = os.listdir(directoryPath)

for content in contents:
  print(content)