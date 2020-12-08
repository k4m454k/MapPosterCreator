import argparse
import logging
import webbrowser

from map_poster_creator.color_schemes import base_color_scheme
from map_poster_creator.main import create_poster
from map_poster_creator import __version__

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def get_root_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='mapoc', description="Map Poster Creator")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + str(__version__))

    return parser


def add_poster_create_subparser(parent_parser) -> argparse.ArgumentParser:
    poster_create_parser = parent_parser.add_parser('create', description='Make Poster')
    poster_create_parser.add_argument('--shp_path', help='Path to shp folder. '
                                                         'Type "mapoc misc shp" to download.', required=True)
    poster_create_parser.add_argument(
        '--geojson', help='Path to geojson file with boundary polygon. '
                          'Type "mapoc misc geojson" to create and download.',
        required=True,
    )
    poster_create_parser.add_argument(
        '--colors', help=f'Provide colors. '
                         f'eq "--colors white black coral". '
                         f'Default: "white". '
                         f'Available colors: {", ".join(base_color_scheme.keys())}',
        default=["white"],
        nargs="+",
    )
    poster_create_parser.add_argument(
        '--output_prefix',
        help='Output file prefix. eq. "{OUTPUT_PREFIX}_{COLOR}.png". Default: "map"',
        type=str,
        default="map"
    )

    return poster_create_parser


def add_misc_shp_subparser(parent_parser) -> argparse.ArgumentParser:
    misc_parser = parent_parser.add_parser('shp', description='Shp download')
    return misc_parser


def add_misc_geojson_subparser(parent_parser) -> argparse.ArgumentParser:
    misc_parser = parent_parser.add_parser('geojson', description='Create geoJSON')
    return misc_parser


def add_poster_subparsers(parser_group) -> argparse.ArgumentParser:
    poster_commands_parser = parser_group.add_parser(
        'poster',
        description='Create Map Poster',
        help='Poster creation',
    )
    poster_commands_parser_group = poster_commands_parser.add_subparsers(
        title='poster management commands',
        description='Create poster',
        help='Additional help for available commands',
        dest='poster_commands',
    )

    add_poster_create_subparser(poster_commands_parser_group)

    return poster_commands_parser


def add_misc_subparsers(parser_group) -> argparse.ArgumentParser:
    misc_commands_parser = parser_group.add_parser(
        'misc',
        description='Misc services',
        help='Misc services',
    )
    misc_commands_parser_group = misc_commands_parser.add_subparsers(
        title='misc management commands',
        description='misc',
        help='Additional help for available commands',
        dest='misc_commands',
    )

    add_misc_shp_subparser(misc_commands_parser_group)
    add_misc_geojson_subparser(misc_commands_parser_group)

    return misc_commands_parser


def process_misc_service_call(args: argparse.Namespace) -> None:
    command = args.misc_commands
    if command == 'shp':
        webbrowser.open_new_tab("https://download.geofabrik.de/")

    if command == "geojson":
        webbrowser.open_new_tab("https://geojson.io/")


def process_poster_service_call(args: argparse.Namespace) -> None:
    command = args.poster_commands

    shp_path = args.shp_path
    geojson = args.geojson
    colors = args.colors
    output_prefix = args.output_prefix

    if command == 'create':
        create_poster(
            base_shp_path=shp_path,
            geojson_path=geojson,
            colors=colors,
            layers=[""],
            config={"none": None},
            output_prefix=output_prefix,
        )
        return


def map_poster(argv=None) -> None:
    parser = get_root_parser()
    poster_creator_services_parser_group = parser.add_subparsers(
        title='Available Map Poster services',
        description='Services that Map Poster provides.',
        help='Additional help for available services',
        dest='map_poster_services',
    )
    add_poster_subparsers(poster_creator_services_parser_group)
    add_misc_subparsers(poster_creator_services_parser_group)

    args = parser.parse_args(argv)

    service = args.map_poster_services
    available_services = {
        'poster': process_poster_service_call,
        'misc': process_misc_service_call,
    }
    if not service:
        parser.print_help()
        parser.print_usage()
        return
    available_services[service](args)


if __name__ == '__main__':
    map_poster()
