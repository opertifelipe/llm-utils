import typer
import logging
from typing_extensions import Annotated


logger = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def test():
    pass