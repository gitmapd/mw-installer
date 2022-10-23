from tabulate import tabulate
import requests
import typer
from itertools import islice
app = typer.Typer(add_completion=False)
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def exts_url():
    url="https://www.mediawiki.org/w/api.php"
    params = {
    'action': 'query',
    'format':'json',
    'meta':'siteinfo',
    'formatversion':2,
    'siprop':'extensions'
    }
    return url,params 
lista={}
def request_url():
    url,params=exts_url()
    resp = requests.get(url,params=params).json()
    resp = resp['query']['extensions']
    for ext in resp:
        if 'vcs-url' in ext:
            lista[ext['name']]=ext['vcs-url'].split('/')[-1]
    return lista
@app.command()
def prints():
    for l,v in lista:
        table=[[l,v]]
        typer.secho(tabulate(table,tablefmt="pretty"),fg=typer.colors.BRIGHT_GREEN)


def main():
    app()


if __name__ == "__main__":  # ensure importing the script will not execute
    main()  
