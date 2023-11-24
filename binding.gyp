{
    "targets": [
        {
            "target_name": "colorflow",
            "cflags!": [ "-fno-exceptions" ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "sources": [
                "native/colorflow.cpp"
            ],
            "include_dirs": [
                "/native/include"
            ],
            "libraries": [
                "/usr/local/lib/libcolorflow.a",
                "/usr/local/lib/libbmp.a",
                "-lpng", 
                "-ljpeg"
            ]
        }
    ]
}