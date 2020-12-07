import json
import logging
from dataclasses import dataclass
from typing import Dict, List

from shapely.geometry import Polygon

logger = logging.getLogger(__name__)


@dataclass
class MapGeometry:
    top: float
    bottom: float
    left: float
    right: float
    center: List[float]


def get_polygon_from_geojson(geojson_path: str) -> Polygon:
    with open(geojson_path) as gjf:
        features: list = json.load(gjf).get("features")

    if not features:
        raise ValueError(f"Features not found in GeoJSON {geojson_path}")

    if len(features) > 1:
        logger.warning(f"Found {len(features)} features. Be use first")

    first_feature, *_ = features
    if not first_feature.get("type") == "Feature":
        raise ValueError(f"Invalid feature type {first_feature.get('type')}. Expected 'Feature'")

    geometry: dict = first_feature.get("geometry")
    if not geometry.get('type') == "Polygon":
        raise ValueError(f"Invalid geometry type {first_feature.get('type')}. Expected 'Polygon'")

    coordinates: list = geometry.get("coordinates")
    if not coordinates:
        raise ValueError(f"Coordinates not found. Check GeoJSON")

    if len(coordinates) > 1:
        logger.warning(f"Found {len(coordinates)} polygons. Be use first")

    first_coords, *_ = coordinates
    polygon = Polygon(first_coords)

    return polygon


def get_map_geometry_from_poly(poly: Polygon) -> MapGeometry:
    x1, y1, x2, y2 = poly.bounds
    top = min(y1, y2)
    bottom = max(y1, y2)
    left = min(x1, x2)
    right = max(x1, x2)
    center = [(top + bottom) / 2, (left + right) / 2]
    geometry = MapGeometry(top=top, bottom=bottom, left=left, right=right, center=center)
    return geometry
