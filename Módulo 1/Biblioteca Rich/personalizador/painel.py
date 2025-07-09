"""Módulo de painel usando rich."""

from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_info(texto: str, isArquivo: bool):
    """Exibe um painel com informações simples."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    panel = Panel(texto, title="Informação", subtitle="Painel padrão", style="green")
    console.print(panel)

def painel_alerta(texto: str, isArquivo: bool):
    """Exibe um painel de alerta com borda vermelha."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    panel = Panel(texto, title="⚠️ Alerta!", border_style="red")
    console.print(panel)
