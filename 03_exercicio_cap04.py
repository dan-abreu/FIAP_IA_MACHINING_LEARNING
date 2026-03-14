OPCOES_VALIDAS = ("PLAYSTATION", "XBOX", "NINTENDO")
TOTAL_MEMBROS = 5


def ler_voto(numero_membro: int) -> str:
    while True:
        voto = input(
            f"Digite o voto do membro {numero_membro} "
            f"({', '.join(OPCOES_VALIDAS)}): "
        ).strip().upper()

        if voto in OPCOES_VALIDAS:
            return voto

        print("Voto invalido. Escolha apenas: PLAYSTATION, XBOX ou NINTENDO.")


def main() -> None:
    votos = {opcao: 0 for opcao in OPCOES_VALIDAS}

    for membro in range(1, TOTAL_MEMBROS + 1):
        voto = ler_voto(membro)
        votos[voto] += 1

    maior_quantidade = max(votos.values())
    vencedores = [console for console, qtd in votos.items() if qtd == maior_quantidade]

    print("\n--- RESULTADO FINAL ---")

    if len(vencedores) == 1:
        console_escolhido = vencedores[0]
        print(f"Console escolhido: {console_escolhido}")
        print(f"Quantidade de votos: {maior_quantidade}")
        return

    print("Empate entre os consoles:")
    for console in vencedores:
        print(f"- {console}: {maior_quantidade} votos")


if __name__ == "__main__":
    main()
