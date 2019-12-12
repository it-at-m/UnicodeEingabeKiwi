#!/bin/bash
set -ex

SVG=$1
SIZE=(16 24 32 64)

echo Making bitmaps from your svg...
for i in ${SIZE[@]}; do
  inkscape -e "favicon-$i.png" -w $i -h $i --without-gui $SVG
done

#echo Compressing...
## Replace with your favorite (e.g. pngquant)
# optipng -o7 favicon-*.png
#pngquant -f --ext .png favicon-*.png --posterize 4 --speed 1

echo Converting to favicon.ico...
convert $(ls -v favicon-*.png) favicon.ico

rm -f favicon-*.png
