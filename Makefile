libcolorflow: native/include/libnsbmp.c native/colorflow.c
	gcc -c -Wall -Werror -fPIC native/include/libnsbmp.c
	ar rcs libbmp.a libnsbmp.o
	rm libnsbmp.o
	gcc -c -Wall -Werror -fPIC native/colorflow.c
	ar rcs libcolorflow.a colorflow.o 
	rm colorflow.o