{
  "targets": [
    {
      "target_name": "blst_wrap",
      "sources": [ "blst_wrap.cpp" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "conditions": [
        ["OS=='win'", {
          "cflags": [
            "/EHsc"
          ]
        }],
         ["OS == 'mac'", {
          "OTHER_CPLUSPLUSFLAGS" : [ "-std=c++11", "-stdlib=libc++" ],
          "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
          "xcode_settings": {
           "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
           "GCC_ENABLE_CPP_RTTI": "YES",
           "MACOSX_DEPLOYMENT_TARGET": "10.12",
           "CLANG_CXX_LANGUAGE_STANDARD": "c++11"
          }
        }],
      ]
    }
  ]
}