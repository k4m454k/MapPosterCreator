# Map Poster Creator

![main window](https://raw.githubusercontent.com/k4m454k/MapPosterCreator/master/pics/msk_c.png?raw=true)


## Valriable Colors

### `white`
![white](https://raw.githubusercontent.com/k4m454k/MapPosterCreator/master/pics/msk_white.png?raw=true)

### `black`
![black](https://raw.githubusercontent.com/k4m454k/MapPosterCreator/master/pics/msk_black.png?raw=true)

### `coral`
![coral](https://raw.githubusercontent.com/k4m454k/MapPosterCreator/master/pics/msk_coral.png?raw=true)


## Install:

`pip install map-poster-creator`

### Deps

#### Linux
- `apt-get install libgeos-dev`

#### Windows 
thanks [Lamroy95](https://github.com/Lamroy95) for Windows instruction 
- Manually download and install two python packages (GDAL and Fiona):
  - Download [GDAL .whl file](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal) for your version of python (Python 3.8 - ...cp38....whl)  
  - Download [Fiona .whl file](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona)  
  - Install GDAL: `pip install path\to\gdal.whl`  
  - Install Fiona: `pip install path\to\fiona.whl`  
  - Finally, install map-poster-creator: `pip install map-poster-creator`  
- Or just use Docker =)

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

## TODO

- Add configurable settings for poster size and quality.
- Add the ability to custom color schemes.
- Add Docker image
