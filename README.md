# pykakasi_docker
pykakasi test with docker

what's pykakasi
https://github.com/miurahr/pykakasi

# build and run

```
# build
$ docker build . -t kakasi_test

$ docker run --rm -it -v `pwd`:/usr/src kakasi_test 松井 イチロー かわさき SHINJO           
matsui
ichiro-
kawasaki
SHINJO

$ docker run --rm -it -v `pwd`:/usr/src kakasi_test --verbose 松井 イチロー かわさき SHINJO 
松井
matsui
イチロー
ichiro-
かわさき
kawasaki
SHINJO
SHINJO

$ docker run --rm -it -v `pwd`:/usr/src kakasi_test --verbose "松井 イチロー かわさき SHINJO"
松井 イチロー かわさき SHINJO
matsui ichiro- kawasaki SHINJO
```
