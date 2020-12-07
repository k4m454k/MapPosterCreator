# OSM Map Poster Creator

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


## Usage:

1. Create geojson file with one poly. https://geojson.io/
2. Download shp archive for region https://download.geofabrik.de/ eq: `central-fed-district-latest-free.shp.zip`
3. Unpack `*.free.shp.zip` archive to some folder `PATH_TO_SHP_DIR`
```
# mapoc poster create --shp_path PATH_TO_SHP_DIR --geojson PATH_TO_GEOJSON --colors white black coral

```

