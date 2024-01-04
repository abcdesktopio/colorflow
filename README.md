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

You will also need to insall Imlib2 by running the following command
```
apt-get update && apt-get install -y  --no-install-recommends \
        libimlib2\
        libimlib2-dev
```

## How to use it

You will first have to clone the repository
```
git clone https://github.com/abcdesktopio/colorflow.git
``` 
Next you have to build the module by running ```make build```  
Now you can use the module as it is shown in the app.js example file.

## Sources 

- Imlib2 : https://docs.enlightenment.org/api/imlib2/html/

