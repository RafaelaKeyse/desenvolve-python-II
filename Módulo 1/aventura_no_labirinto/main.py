"""
Arquivo principal que inicia o jogo e gerencia o menu e argumentos da CLI.
"""

import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import Jogador
from aventura_pkg.utils import imprimir_menu, imprime_instrucoes
from rich import print

def jogar(labirinto, jogador):
    """
    Laço principal do jogo: mostra o labirinto e lê movimentos até vitória ou saída.
    """
    while True:
        print(f"\nPontuação: {jogador.pontuacao}")
        imprimir_labirinto(labirinto, jogador.pos)
        comando = input("Mover (WASD) ou Q para sair: ").strip()

        if comando.lower() == "q":
            print("[red]Jogo encerrado.[/red]")
            break

        if jogador.mover(comando):
            jogador.pontuar()

            # Verifica se o jogador chegou na saída
            if jogador.pos == (len(labirinto) - 1, len(labirinto[0]) - 1):
                print(f"\n[bold green]Parabéns, {args.name}! Você venceu o labirinto! 🏆[/bold green]")
                print(f"Sua pontuação final foi: [yellow]{jogador.pontuacao}[/yellow]")
                break
        else:
            print("[red]Movimento inválido![/red]")

# -------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")

    parser.add_argument("--name", required=True, help="Nome do(a) jogador(a)")
    parser.add_argument("--dificuldade", type=int, default=1, choices=[1, 2, 3], help="Dificuldade do jogo (1-3)")
    parser.add_argument("--color", help="Cor principal do jogo (opcional)")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa som (não implementado)")
    parser.add_argument("--help-custom", action="help", help="Mostra esta mensagem de ajuda personalizada")

    args = parser.parse_args()

    print(f"\nBem-vindo(a), {args.name}!")

    while True:
        imprimir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        match opcao:
            case "1":
                imprime_instrucoes()
            case "2":
                labirinto = criar_labirinto(dificuldade=args.dificuldade)
                jogador = Jogador(labirinto)
                jogar(labirinto, jogador)
            case "3":
                labirinto = criar_labirinto(dificuldade=args.dificuldade)
                caminho = []
                visitados = set()

                from aventura_pkg.jogador import resolver_labirinto_recursivo, animar_solucao

                sucesso = resolver_labirinto_recursivo(
                    labirinto, 0, 0, caminho, visitados
                )

                if sucesso:
                    print("[bold cyan]Mostrando solução automática...[/bold cyan]")
                    animar_solucao(labirinto, caminho)
                    print("[bold green]Solução concluída![/bold green]")
                else:
                    print("[red]Não foi possível encontrar caminho.[/red]")
            case "4":
                print("[bold]Saindo do jogo... Até logo![/bold]")
                break
            case _:
                print("[red]Opção inválida. Tente novamente.[/red]")
