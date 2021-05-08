# Map Poster Creator

**Map Poster Creator** - script for creating beautiful road maps of any cities, zones, sections according to OSM data. 
You can add green areas, roads, rivers, ponds, lakes to the map.
There are several ready-made color schemes, but you can easily add your own colors.

The project is provided as-is.

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

### Colors

#### Add new color scheme

Add a new color scheme or rewrite available color scheme.

```bash
usage: mapoc color add [-h] --name NAME --facecolor FACECOLOR --water WATER --greens GREENS --roads ROADS

List available colors

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Name of color scheme. eq. "blue"
  --facecolor FACECOLOR
                        MatPlot face hex color. eq. "#ffffff"
  --water WATER         MatPlot water hex color. eq. "#ffffff"
  --greens GREENS       MatPlot greens hex color. eq. "#ffffff"
  --roads ROADS         MatPlot roads hex color. eq. "#ffffff"

```

Example:
```bash
$ mapoc color add --name "coffee" --facecolor "#433633" --water "#5c5552" --greens "#8f857d" --roads "#decbb7" 
```

#### List available color schemes

```bash
$ mapoc color list
```

## TODO

- Add configurable settings for poster size and quality.
- Add Docker image
