# Colorflow

Colorflow is a Node.js module that allows you to get the HEXA code for a background color to set based on an image.  
The supported file formats for the images are PNG, JPEG and Bitmap.

## Requirements

- binutils
- make
- gcc
- g++
- Node.js
- npm (Node.js package manager)

You will also need to insall libpng and libjpeg by running the following command
```
apt-get update && apt-get install -y  --no-install-recommends \
        libpng-dev \
	    libjpeg-dev 
```

## How to use it

You will first have to clone the repository
```
git clone https://github.com/abcdesktopio/colorflow.git
``` 
Next you have to build the module by running ```make build```  
Now you can use the module as it is shown in the app.js example file.

## Sources 

- libpng : https://github.com/glennrp/libpng
- libjpeg : https://github.com/LuaDist/libjpeg/tree/master
- libnsbmp : https://github.com/uobikiemukot/idump/tree/master 

