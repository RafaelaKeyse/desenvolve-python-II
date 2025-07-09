import argparse
from personalizador import layout, painel, progresso, estilo

# Mapeamento de módulos e funções disponíveis
MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo,
}

FUNCOES = {
    "layout": ["exibir_layout_simples", "exibir_layout_mensagem"],
    "painel": ["painel_info", "painel_alerta"],
    "progresso": ["barra_simples", "barra_detalhada"],
    "estilo": ["texto_colorido", "texto_negrito"]
}

# Configuração do argparse
parser = argparse.ArgumentParser(
    description="Imprime texto formatado com o módulo personalizador usando a biblioteca Rich."
)

parser.add_argument(
    "texto",
    help="Texto direto ou caminho do arquivo a ser impresso"
)

parser.add_argument(
    "-a", "--arquivo",
    action="store_true",
    help="Indica que o argumento é o caminho para um arquivo"
)

parser.add_argument(
    "-m", "--modulo",
    required=True,
    choices=MODULOS.keys(),
    help="Escolhe o módulo (layout, painel, progresso, estilo)"
)

parser.add_argument(
    "-f", "--funcao",
    required=True,
    help=(
        "Escolhe a função a ser usada no módulo. "
        "Opções: layout = exibir_layout_simples, exibir_layout_mensagem; "
        "painel = painel_info, painel_alerta; "
        "progresso = barra_simples, barra_detalhada; "
        "estilo = texto_colorido, texto_negrito"
    )
)

args = parser.parse_args()

# Verificação e execução da função
modulo = MODULOS[args.modulo]

if args.funcao not in FUNCOES[args.modulo]:
    print(f"Função inválida para o módulo '{args.modulo}'.")
    print(f"Funções disponíveis: {FUNCOES[args.modulo]}")
else:
    funcao_escolhida = getattr(modulo, args.funcao)
    funcao_escolhida(args.texto, args.arquivo)
