
m tabulate import tabulate
import typer
app = typer.Typer(add_completion=False)
import pkg_resources
import requests
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def get_exts():
    lista={}
    url="https://www.mediawiki.org/w/api.php"
    params = {
    'action': 'query',
    'format':'json',
    'meta':'siteinfo',
    'formatversion':2,
    'siprop':'extensions'
    }

    resp = requests.get(url,params=params).json()
    resp = resp['query']['extensions']
    for ext in resp:
        if 'vcs-url' in ext:
            lista[ext['name']]=ext['vcs-url'].split('/')[-1]
    return lista
@app.command()
def prints():
    ten = take(10,get_exts().items())
    for l,v in ten:
        table=[[l,v]]
        typer.secho(tabulate(table,tablefmt="pretty"),fg=typer.colors.BRIGHT_GREEN)


def main():
    app()


if __name__ == "__main__":  # ensure importing the script will not execute
    main()
