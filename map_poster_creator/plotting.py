import math

from geopandas import GeoDataFrame
from matplotlib import pyplot as plt

from map_poster_creator.geojson import MapGeometry
from map_poster_creator.logs import log_processing


def road_width(speed: int) -> float:
    if speed in range(0, 30):
        return 0.05
    if speed in range(30, 50):
        return 0.1
    if speed in range(50, 90):
        return 0.2
    if speed in range(90, 200):
        return 0.3
    return 0.4


def plot_and_save(
        roads: GeoDataFrame,
        water: GeoDataFrame,
        greens: GeoDataFrame,
        color: dict,
        geometry: MapGeometry,
        path: str,
        dpi=300,
):

    ax = set_subplot(color)

    plot_water(ax, color, water)

    plot_greens(ax, color, greens)

    plot_roads(ax, color, roads)

    aspect = 1 / math.cos(math.pi / 180 * geometry.center[0])
    ax.set_aspect(aspect)
    ax.set_ylim((geometry.bottom, geometry.top))
    ax.set_xlim((geometry.left, geometry.right))
    plt.axis('off')
    save_image(dpi, path)


@log_processing
def save_image(dpi, path):
    plt.savefig(path, bbox_inches='tight', dpi=dpi)


@log_processing
def set_subplot(color):
    plt.clf()
    f, ax = plt.subplots(1, figsize=(19, 19), facecolor=color['facecolor'])
    return ax


@log_processing
def plot_water(ax, color, water):
    water.plot(ax=ax, color=color['water'], linewidth=0.1)


@log_processing
def plot_greens(ax, color, greens):
    greens.plot(ax=ax, color=color['greens'], linewidth=0.1)


@log_processing
def plot_roads(ax, color, roads):
    roads.plot(
        ax=ax,
        color=color['roads'],
        linewidth=[road_width(d) for d in roads.speeds]
    )