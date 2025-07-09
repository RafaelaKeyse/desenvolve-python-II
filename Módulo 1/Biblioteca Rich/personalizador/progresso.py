"""Módulo de progresso usando rich."""

from rich.console import Console
from rich.progress import track, Progress
import time

console = Console()

def barra_simples(texto: str, isArquivo: bool):
    """Exibe uma barra de progresso simples com print de texto ao final."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    for passo in track(range(10), description="Carregando..."):
        time.sleep(0.1)
    console.print(f"[bold green]Finalizado:[/bold green] {texto}")

def barra_detalhada(texto: str, isArquivo: bool):
    """Exibe barra com progresso detalhado."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arq:
            texto = arq.read()
    with Progress() as progress:
        tarefa = progress.add_task("Processando...", total=100)
        while not progress.finished:
            progress.update(tarefa, advance=10)
            time.sleep(0.2)
    console.print(f"[bold blue]Processo concluído:[/bold blue] {texto}")
