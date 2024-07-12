#!/bin/bash

cd ..

rm -rf ./lambda
rm ./lambda.zip

mkdir ./lambda
cp -R keygen-core/* ./lambda
cp -R keygen-plugins/* ./lambda
cd ./lambda || exit
zip -r9 ../lambda.zip .
cd ..
rm -rf ./lambda