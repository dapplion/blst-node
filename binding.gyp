{
  "targets": [
    {
      "target_name": "blst_wrap",
      "sources": [ "blst_wrap.cpp" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "conditions": [
         ["OS == 'mac'", {
          "xcode_settings": {
            "MACOSX_DEPLOYMENT_TARGET": "10.7",
            "GCC_C_LANGUAGE_STANDARD": "c89",
            "WARNING_CFLAGS": [
              "-pedantic",
              "-Wcast-align",
              "-Wno-implicit-fallthrough",
              "-Wno-long-long",
              "-Wno-overlength-strings",
              "-Wshadow"
            ]
          }
        }],
      ]
    }
  ]
}