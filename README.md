# notrealface.py
Get random virtual face from thispersondoesnotexists.com and thiscatdoesnotexit.com

# How to use
```sh
usage: notrealface.py [-h] [--type {human,cat}] [--nb NB] [--path PATH]

optional arguments:
  -h, --help          show this help message and exit
  --type {human,cat}  type of face (default is 'human')
  --nb NB             number of faces to generate (default is '1')
  --path PATH         where to save the images (default is './')
```

# Examples

### Generate one human face in current directory:
```sh
x4n4@ares:~/randomDir$ python3 notrealface.py
```

### Set optional args for total liberty:
```sh
x4n4@ares:~/randomDir$ ls
notrealface.py
x4n4@ares:~/randomDir$ mkdir data
x4n4@ares:~/randomDir$ python3 notrealface.py --type="cat" --nb="42" --path="./data"
x4n4@ares:~/randomDir$ ls ./data/
face-0.jpeg   face-14.jpeg  face-19.jpeg  face-23.jpeg  face-28.jpeg  face-32.jpeg  face-37.jpeg  face-41.jpeg  face-8.jpeg
face-10.jpeg  face-15.jpeg  face-1.jpeg   face-24.jpeg  face-29.jpeg  face-33.jpeg  face-38.jpeg  face-4.jpeg   face-9.jpeg
face-11.jpeg  face-16.jpeg  face-20.jpeg  face-25.jpeg  face-2.jpeg   face-34.jpeg  face-39.jpeg  face-5.jpeg
face-12.jpeg  face-17.jpeg  face-21.jpeg  face-26.jpeg  face-30.jpeg  face-35.jpeg  face-3.jpeg   face-6.jpeg
face-13.jpeg  face-18.jpeg  face-22.jpeg  face-27.jpeg  face-31.jpeg  face-36.jpeg  face-40.jpeg  face-7.jpeg
```

### There are default value for each parameters, nothing is mandatory:
```sh
x4n4@ares:~/randomDir$ python3 notrealface.py --nb=2
x4n4@ares:~/randomDir$ ls
data  face-0.jpeg  face-1.jpeg  notrealface.py
x4n4@ares:~/randomDir$ 
```

# BTW
There is a time of two seconds between each download to avoid saturating the servers and to avoid having twice the same image
