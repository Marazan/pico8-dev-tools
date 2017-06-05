from os import getcwd
from os.path import split, join
import json
import click

GLOBAL_CONFIG = ".weaver_global.json"
CART_CONFIG = "config.json"


def _get_config(name):
    global_config, root = _locate_global_config()
    cart_config, cart_location = _locate_cart_config(root, name)

    config = global_config
    config.update(cart_config)

    config['fs_root'] = root
    config['fs_cart'] = cart_location
    config['short_name'] = name

    return config


def _locate_global_config():
    current_dir = getcwd()
    while True:
        try:
            return json.load(open(join(current_dir, GLOBAL_CONFIG))), current_dir
        except:
            old = current_dir
            current_dir, tail = split(current_dir)
            if current_dir == old:
                raise FileNotFoundError


def _locate_cart_config(root, name):
    cart_location = join(root, 'carts', name, CART_CONFIG)
    try:
        return json.load(open(cart_location)), cart_location
    except:
        click.echo("Could not find cart")
        raise FileNotFoundError


@click.group()
def cli():
    """Welcome to pico dev tools"""


@cli.command()
@click.pass_context
def showcarts(ctx):
    click.echo("Show Carts")


@cli.command()
@click.pass_context
@click.argument("name")
def build(ctx, name):
    click.echo("Building {}".format(name))
    config = _get_config(name)
    print(config)


if __name__ == "__main__":
    cli()
