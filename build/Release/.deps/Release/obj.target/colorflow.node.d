cmd_Release/obj.target/colorflow.node := g++ -o Release/obj.target/colorflow.node -shared -pthread -rdynamic -m64  -Wl,-soname=colorflow.node -Wl,--start-group Release/obj.target/colorflow/native/colorflow.o -Wl,--end-group /usr/local/lib/libcolorflow.a /usr/local/lib/libbmp.a -lpng -ljpeg