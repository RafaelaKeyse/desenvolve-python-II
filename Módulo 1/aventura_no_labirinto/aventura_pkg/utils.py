
"""
Módulo utilitário com funções de menu e instruções.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def imprimir_menu():
    """Exibe o menu principal do jogo."""
    console.print(Panel.fit(
        "[bold cyan]🧩 Aventura no Labirinto 🧩[/bold cyan]\n"
        "[green]1.[/] Instruções\n"
        "[green]2.[/] Jogar\n"
        "[green]3.[/] Assistir solução recursiva\n"
        "[green]4.[/] Sair"
    ))

def imprime_instrucoes():
    """Lê e imprime o conteúdo de instruções.txt formatado."""
    try:
        with open("instrucoes.txt", "r", encoding="utf-8") as f:
            texto = f.read()
        console.print(Panel.fit(texto, title="📘 Instruções", subtitle="Use W A S D para se mover"))
    except FileNotFoundError:
        console.print("[red]Arquivo instrucoes.txt não encontrado.[/red]")
