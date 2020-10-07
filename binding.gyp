{
  "targets": [
    {
      "target_name": "blst_wrap",
      "sources": [ "blst_wrap.cpp" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
    }
  ]
}