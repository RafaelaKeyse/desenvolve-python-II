"""Módulo de layout usando rich."""

from rich.console import Console
from rich.layout import Layout

console = Console()

def exibir_layout_simples(texto: str, isArquivo: bool):
    """Exibe um layout simples com o texto ou conteúdo do arquivo."""
    layout = Layout()
    layout.split_row(Layout(name="esquerda"), Layout(name="direita"))

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()

    layout["esquerda"].update(texto)
    layout["direita"].update("-> Layout demonstrado!")
    console.print(layout)

def exibir_layout_mensagem(texto: str, isArquivo: bool):
    """Exibe uma mensagem com destaque no layout."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    layout = Layout(name="mensagem")
    layout.update(f"[bold cyan]{texto}[/bold cyan]")
    console.print(layout)
