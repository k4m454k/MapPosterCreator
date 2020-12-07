import setuptools

from map_poster_creator import __version__, __author__, __author_email__

setuptools.setup(
    name="map_poster_creator",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description="Map Poster Creator",
    url="https://github.com/k4m454k/MapPosterCreator",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'mapoc = map_poster_creator.entrypoints:map_poster',
        ],
    },
    install_requires=open("requirements.txt").read().split(),
    python_requires='>=3.7',
)
