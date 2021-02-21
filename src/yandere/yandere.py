from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time
import requests
import sys
import pathlib
import os
start = time.time()

print("""yande.re scraper\n""")

site = "yande.re"
last_tag = "../spell.txt"
with open(last_tag) as f:
    content = f.read().splitlines()

if len(sys.argv) < 3:
    sys.exit(f"Usage: {sys.argv[0]} [pages] [tags]\nMultiple tags separated by (comma)")

for tag in sys.argv[2:]:

    babi = tag.translate(str.maketrans({',': ' ', '[': '(', ']': ')', 'X': '/'}))
    print(f"tags: {babi}")
    name, ext = site.split('.')[-2:]
    ven = name+"_"+babi
    for line in content:
        print(f"last_tags: {line}")
        spell = babi + " " + line
        pathlib.Path(f"./{ven}").mkdir(exist_ok=True)

    for pid in range(0, int(sys.argv[1])):
        response = requests.get(f"https://yande.re/post.xml?limit=50&tags={spell}&page={pid}")
        content = BeautifulSoup(response.content, "html.parser")

        for link in content.find_all("post"):
            image_url = link.get("file_url")
            image_url_split = urlparse(image_url).path.split("/")
            file = image_url_split[len(image_url_split) - 1]

            image = requests.get(image_url)
            print(f"getting {image_url} === {file}")

            open(f"./{ven}/{file}", "wb").write(image.content)

end = time.time()

totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(ven):
    print('Saved in : ', base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1


# print('\nRetrieved',totalFiles,'images.')
print('\nTags: ', babi)
print('Total:', (totalDir + totalFiles))

hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Elapsed: ","{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))