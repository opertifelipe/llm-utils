import typer
from llm_utils.cli.main_nlp import app as app_nlp

app = typer.Typer()

app.add_typer(app_nlp, name="nlp")