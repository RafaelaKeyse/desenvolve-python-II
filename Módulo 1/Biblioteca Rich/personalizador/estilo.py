"""Módulo de estilos usando rich."""

from rich.console import Console
from rich.text import Text

console = Console()

def texto_colorido(texto: str, isArquivo: bool):
    """Exibe texto com cores diferentes."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    txt = Text(texto, style="bold magenta")
    console.print(txt)

def texto_negrito(texto: str, isArquivo: bool):
    """Exibe texto em negrito e azul."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    txt = Text(texto, style="bold blue")
    console.print(txt)
