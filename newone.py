import typer
import os
from dotenv import load_dotenv
from pathlib import Path
from rich.console import Console
from rich.table import Table
from model import Extension
from database import get_all_ext, insert_ext
from get_ext import get_specific
console = Console()
load_dotenv()
app = typer.Typer()


@app.command(short_help='adds an extension')
def add(name: str, version: str):
    extname, url=get_specific(name,version)
    extension = Extension(extname, version, url)
    insert_ext(extension)
    typer.echo(f"adding {name}, {version}, {url}")
    show()

@app.command()
def show():
    exts = get_all_ext()
    console.print("[bold magenta]Extensions[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Name", min_width=20)
    table.add_column("Version", min_width=12, justify="right")
    table.add_column("Url", min_width=12, justify="right")

    for idx, ext in enumerate(exts, start=1):
       table.add_row(str(idx), ext.name, ext.version, ext.url)
    console.print(table)

@app.command(short_help='lists extensions')
def list(path=None):
    if path is None:
        path = Path(f'{os.getenv("path")}')
        dirs=[f for f in path.iterdir() if f.is_dir()]
        folders={}
        for i,d in enumerate(dirs):
            folders[i]=d
        for i,k in folders.items():
            print(k)

if __name__ == "__main__":
    app()
