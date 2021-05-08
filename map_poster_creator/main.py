from typing import Tuple, List, Dict, Union

import fiona  # noqa For Apple Silicon (M1) CPU
from geopandas import GeoDataFrame
from shapely.geometry import Polygon

from map_poster_creator.color_schemes import get_color_schemes
from map_poster_creator.geojson import get_polygon_from_geojson, get_map_geometry_from_poly, MapGeometry
from map_poster_creator.logs import log_processing, logging
from map_poster_creator.plotting import plot_and_save

logger = logging.getLogger(__name__)


@log_processing
def get_roads_data(shp_path: str) -> GeoDataFrame:
    roads = GeoDataFrame.from_file(f"{shp_path}/gis_osm_roads_free_1.shp", encoding='utf-8')
    return roads  # TODO: Add Path or os.path


@log_processing
def get_water_data(shp_path: str) -> GeoDataFrame:
    water = GeoDataFrame.from_file(f"{shp_path}/gis_osm_water_a_free_1.shp", encoding='utf-8')
    return water  # TODO: Add Path or os.path


@log_processing
def get_greens_data(shp_path: str) -> GeoDataFrame:
    greens = GeoDataFrame.from_file(f"{shp_path}/gis_osm_pois_a_free_1.shp", encoding='utf-8')
    return greens  # TODO: Add Path or os.path


@log_processing
def get_boundary_shape(geojson) -> Tuple[Polygon, MapGeometry]:
    poly = get_polygon_from_geojson(geojson)
    geometry = get_map_geometry_from_poly(poly)
    return poly, geometry


@log_processing
def preprocessing_roads(poly: Polygon, roads: GeoDataFrame) -> GeoDataFrame:
    town = roads.loc[roads['geometry'].apply(lambda g: poly.contains(g))].copy()
    town = town[~town.fclass.isin(['footway', "steps"])]
    town['speeds'] = [speed for speed in town['maxspeed']]
    return town


@log_processing
def preprocessing_other(poly: Polygon, dataframe: GeoDataFrame) -> GeoDataFrame:
    town = dataframe.loc[dataframe['geometry'].apply(lambda g: poly.contains(g))].copy()
    return town


def create_poster(
        base_shp_path: str,
        geojson_path: str,
        colors: Union[List[Union[Dict, str]], None],
        layers: List[str],
        config: dict,
        output_prefix: str,
        user_color_scheme: bool = False,
):
    poly, geometry = get_boundary_shape(geojson=geojson_path)
    roads = get_roads_data(base_shp_path)
    water = get_water_data(base_shp_path)
    greens = get_greens_data(base_shp_path)
    roads_df = preprocessing_roads(poly=poly, roads=roads)
    water_df = preprocessing_other(poly=poly, dataframe=water)
    greens_df = preprocessing_other(poly=poly, dataframe=greens)
    # TODO: Support user color scheme
    for color in colors:
        if color not in get_color_schemes().keys():
            logger.warning(f"Color {color} not found in base color scheme. "
                           f"Available colors: {', '.join(get_color_schemes().keys())}")
        print("")
        print(f"Plot and Save {color} map")
        plot_and_save(
            roads=roads_df,
            water=water,
            greens=greens_df,
            geometry=geometry,
            path=f'{output_prefix}_{color}.png',
            dpi=1200,
            color=get_color_schemes()[color]
        )
