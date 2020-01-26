#! /bin/sh

docker run -it -v ~/CUHackit2020/mnt:/mnt -p 5000:5000 test:test $@
