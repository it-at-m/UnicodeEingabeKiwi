#!/bin/bash
set -ex

SVG=$1
SIZE=(48 72 96 144 192 512)
for i in ${SIZE[@]}; do
  inkscape -e "icon-$ix$i.png" -w $i -h $i --without-gui $SVG
done
