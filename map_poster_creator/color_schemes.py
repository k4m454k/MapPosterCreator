import json
import logging
import os
import re
from pathlib import Path
from typing import Union, Tuple, List, Dict

from map_poster_creator.config import MAPOC_USER_PATH, USER_COLORS_SCHEME_FILE

logger = logging.getLogger(__name__)

base_color_scheme = {
    "black": {
        "facecolor": [0, 0, 0],
        "water": "#383d52",
        "greens": "#354038",
        "roads": "#ffffff",
    },
    "white": {
        "facecolor": [1, 1, 1],
        "water": "#bdddff",
        "greens": "#d4ffe1",
        "roads": "#000000",
    },
    "red": {
        "facecolor": [0.4, 0.12, 0.12],
        "water": "#754444",
        "greens": "#b36969",
        "roads": "#ffffff",
    },
    "coral": {
        "facecolor": [0.67, 0.2, 0.18],
        "water": "#ffffff",
        "greens": "#b36969",
        "roads": "#ffffff",
    },
}


def is_hex_color(hex_color: str):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_color)
    return True if match else False


def hex_to_faceacolor(hex_color: str):
    if not is_hex_color(hex_color):
        raise ValueError(f"{hex_color} is a not hex color. Expected eq. '#ffffff'")

    color = hex_color.strip("#")
    return tuple(1 / 255 * int(color[i:i+2], 16) for i in (0, 2, 4))  # magic asshole-code


def get_color_schemes() -> Dict[str, Dict[str, Union[List[float], Tuple[float]]]]:
    config_path = Path(os.path.expanduser("~")) / MAPOC_USER_PATH / USER_COLORS_SCHEME_FILE
    ensure_user_colors_or_create(config_path)
    with open(config_path, "r") as conf:
        color_scheme = json.load(conf)

    return color_scheme


def ensure_user_colors_or_create(config_path: Path):
    if config_path.is_file():
        return
    if not config_path.parent.is_dir():
        os.makedirs(config_path.parent)

    logger.info(f"User colors config not found!")
    save_user_color_schemes(config_path=config_path, color_schemes=base_color_scheme)


def save_user_color_schemes(config_path: Path, color_schemes: Dict[str, Dict[str, Union[List[float], Tuple[float]]]]):
    with open(config_path, "w") as conf:
        json.dump(color_schemes, conf)
    logger.info(f"Save user colors config: {config_path}")


def compose_user_color_scheme(
        name: str,
        facecolor: Union[Tuple[Union[float, int]], List[Union[float, int]], str],
        water: str,
        greens: str,
        roads: str
) -> Dict[str, Dict[str, Union[List[float], Tuple[float]]]]:
    if isinstance(facecolor, str):
        if not is_hex_color(facecolor):
            raise ValueError(f"{facecolor} is a not hex color. Expected eq. '#ffffff'")
        facecolor = hex_to_faceacolor(facecolor)

    if not all([is_hex_color(val) for val in [water, greens, roads]]):
        raise ValueError(f"Hex color validation error. Expected eq. '#ffffff'")

    new_scheme = {
        name: {
            "facecolor": facecolor,
            "water": water,
            "greens": greens,
            "roads": roads,
        }
    }
    return new_scheme


def add_user_color_scheme(
        name: str,
        facecolor: Union[Tuple[Union[float, int]], List[Union[float, int]], str],
        water: str,
        greens: str,
        roads: str
):
    current_color_schemes = get_color_schemes()
    if name in current_color_schemes.keys():
        logger.warning(f"Color scheme {name} exists. Will be rewrite.")

    new_scheme = compose_user_color_scheme(
        name=name,
        facecolor=facecolor,
        water=water,
        greens=greens,
        roads=roads,
    )

    config_path = Path(os.path.expanduser("~")) / MAPOC_USER_PATH / USER_COLORS_SCHEME_FILE
    current_color_schemes.update(new_scheme)
    save_user_color_schemes(config_path=config_path, color_schemes=current_color_schemes)
