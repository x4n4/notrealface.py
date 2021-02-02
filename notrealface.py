#!/usr/bin/env python3

import sys
import argparse
import requests
import time

"""
usage: notrealface.py [-h] [--type (human,cat,art,horse] [--nb NB] [--path PATH]
"""

def get_face(url, nb, path):
    """ Download [nb] faces from [url] and save it in [path] """
    for i in range(0, nb):
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            print("Error during http request. abort !")
            break
        try:
            with open(f"{path}/fake-{i}.jpeg", 'wb') as f:
                f.write(r.content)
        except IOError:
            print("Please check your --path parameter. abord !")
            break
        time.sleep(2)

if __name__ == "__main__":
    URL = {"human": "https://thispersondoesnotexist.com/image",
           "cat": "https://thiscatdoesnotexist.com/",
           "art": "https://thisartworkdoesnotexist.com/",
           "horse": "https://thishorsedoesnotexist.com/"}
    # Args
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="human",
                        choices=["human", "cat", "art", "horse"],
                        help="type of face (default is 'human')")
    parser.add_argument("--nb", type=int, default=1,
                        help="number of faces to generate (default is '1')")
    parser.add_argument("--path", type=str, default="./",
                        help="where to save the images (default is './')")
    args = parser.parse_args()
    # Set value
    url = URL[args.type]
    nb = args.nb if args.nb >= 1 else 1
    path = args.path
    # Core
    get_face(url=url, nb=nb, path=path)
    # Exit
    sys.exit(0)
