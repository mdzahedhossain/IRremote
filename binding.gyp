{
    "targets": [
      {
        "target_name": "IRremote",
	"product_extension": "node",
	"include_dirs": [ "include", "/usr/local/include" ],
	"libraries": [ "../lib/libpwm.a" ],
        "sources": [ "src/IRremote.cc", "src/SimpleGPIO.cpp" ]
      }
    ]
}
