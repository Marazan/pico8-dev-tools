import click

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
    click.echo("Build {}".format(name)) 

if __name__ == "__main__":
    cli()
