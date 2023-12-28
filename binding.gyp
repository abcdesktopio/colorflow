{
    "targets": [
        {
            "target_name": "colorflow",
            "cflags!": [ "-fno-exceptions", "-Wwrite-strings", "-Wunused-variable"],
            "cflags_cc!": [ "-fno-exceptions",  "-Wwrite-strings", "-Wunused-variable" ],
            "sources": [             
                "native/libnsbmp.cpp",
                "native/libcolorflow.cpp",
                "native/colorflow.cpp"
            ],
            "include_dirs": [
                "/native/include"
            ],
            "libraries": [
                "-lpng", 
                "-ljpeg"
            ]
        }
    ]
}