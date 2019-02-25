import sys
import argparse
import requests
import time

""" Get random virtual face from thispersondoesnotexists.com and thiscatdoesnotexit.com

usage: notrealface.py [-h] [--type {human,cat}] [--nb NB] [--path PATH]

optional arguments:
  -h, --help          show this help message and exit
  --type {human,cat}  type of face (default is 'human')
  --nb NB             number of faces to generate (default is '1')
  --path PATH         where to save the images (default is './')

"""

URL = {"human": "https://thispersondoesnotexist.com/image", "cat": "https://thiscatdoesnotexist.com/"}

def getface(url, nb, path):
    """ Download [nb] faces from [url] and save it in [path] """
    for i in range(0, nb):
        r = requests.get(url)
        if r.status_code == 200:
            try:
                with open("{}/face-{}.jpeg".format(path, i), 'wb') as f:
                    f.write(r.content)
            except IOError as e:
                print(e)
                print("Please check your --path parameter.")
                break
        time.sleep(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="human", choices=["human", "cat"], help="type of face (default is 'human')")
    parser.add_argument("--nb", type=int, default=1, help="number of faces to generate (default is '1')")
    parser.add_argument("--path", type=str, default="./", help="where to save the images (default is './')")
    args = parser.parse_args()
    url = URL[args.type]
    nb = args.nb if args.nb >= 1 else 1
    path = args.path
    getface(url=url, nb=nb, path=path)
    sys.exit(0)
