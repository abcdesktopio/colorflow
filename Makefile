libcolorflow: native/include/libnsbmp.c native/colorflow.c
	gcc -c -Wall -Werror -fPIC native/include/libnsbmp.c
	ar rcs libbmp.a libnsbmp.o
	gcc -c -Wall -Werror -fPIC native/colorflow.c
	ar rcs libcolorflow.a colorflow.o 


clean: colorflow.o libnsbmp.o 
	rm libnsbmp.o
	rm colorflow.o

build: binding.gyp libbmp.a libcolorflow.a
	npm run build

test: colorflow.test.js
	npm test