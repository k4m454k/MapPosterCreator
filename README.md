# Map Poster Creator

![main window](pics/msk_c.png?raw=true)


## Valriable Colors

### `white`
![white](pics/msk_white.png?raw=true)

### `black`
![black](pics/msk_black.png?raw=true)

### `coral`
![coral](pics/msk_coral.png?raw=true)


## Install:

`pip install map-poster-creator`

### Deps

#### Linux
- `apt-get install libgeos-dev`

#### Windows [BIG TROUBLE, 14GB Dependencies]
- Use Docker =)

#### MacOS
- `brew install geos`

## Usage:

1. Create geojson file with one poly. https://geojson.io/
2. Download shp archive for region https://download.geofabrik.de/ eq: `central-fed-district-latest-free.shp.zip`
3. Unpack `*.free.shp.zip` archive to some folder `PATH_TO_SHP_DIR`

```bash
$ mapoc poster create --shp_path PATH_TO_SHP_DIR --geojson PATH_TO_GEOJSON --colors white black coral
```

```bash
$ mapoc poster create -h 
usage: Map Poster Creator poster create [-h] --shp_path SHP_PATH --geojson GEOJSON [--colors COLORS [COLORS ...]] [--output_prefix OUTPUT_PREFIX]

Make Poster

optional arguments:
  -h, --help            show this help message and exit
  --shp_path SHP_PATH   Path to shp folder.type "mapoc misc shp" to download
  --geojson GEOJSON     Path to geojson file with boundary polygon.type "mapoc misc geojson" to create and download
  --colors COLORS [COLORS ...]
                        Provide colors. eq "--colors white black coral". Default: "white". Available colors: black, white, red, coral
  --output_prefix OUTPUT_PREFIX
                        Output file prefix. eq. "{OUTPUT_PREFIX}_{COLOR}.png". Default: "map"
```

```bash
$ mapoc misc -h          
usage: Map Poster Creator misc [-h] {shp,geojson} ...

Misc services

optional arguments:
  -h, --help     show this help message and exit

misc management commands:
  misc

  {shp,geojson}  Additional help for available commands

```