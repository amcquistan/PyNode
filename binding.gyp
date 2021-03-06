{
  "targets": [
    {
      "target_name": "PyNode",
      "sources": [
        "src/main.cpp",
        "src/helpers.cpp"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ['OS=="win"', {
          "variables": {
            "PY_HOME%": "<!(python -c \"import sysconfig;print(sysconfig.get_paths()['data'])\")"
          },
          "include_dirs": [
            "<!(echo <(PY_HOME)\include)"
          ],
          "msvs_settings": {
            "VCLinkerTool": {
              "AdditionalLibraryDirectories": "<!(echo <(PY_HOME)\libs)"
            }
          }
        }],
        ['OS!="win"', {
          "include_dirs": [
            "<!(python-config --cflags)"
          ],
          "libraries": [
            "<!(python-config --ldflags)",
          ]
        }]
      ]
    }
  ]
}
