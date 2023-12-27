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
                "../libcolorflow.a",
                "../libbmp.a",
                "-lpng", 
                "-ljpeg"
            ]
        }
    ]
}