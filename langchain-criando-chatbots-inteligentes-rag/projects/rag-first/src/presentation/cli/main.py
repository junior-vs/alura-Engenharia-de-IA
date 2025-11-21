"""Main entry point for the CLI application."""
import click


@click.group()
@click.version_option(version="0.1.0")
def cli() -> None:
    """RAG-First CLI - A RAG-based application command-line interface."""
    pass


@cli.command()
@click.option("--name", default="World", help="Name to greet")
def hello(name: str) -> None:
    """Say hello."""
    click.echo(f"Hello, {name}!")


@cli.command()
def info() -> None:
    """Display application information."""
    click.echo("RAG-First v0.1.0")
    click.echo("A RAG-based application following Clean Architecture")


if __name__ == "__main__":
    cli()
