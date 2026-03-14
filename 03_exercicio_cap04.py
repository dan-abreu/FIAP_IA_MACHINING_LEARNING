from collections import Counter


OPCOES = ("PLAYSTATION", "XBOX", "NINTENDO")


def main() -> None:
    votos: list[str] = []

    for i in range(1, 6):
        while True:
            voto = input(f"Voto {i} ({', '.join(OPCOES)}): ").strip().upper()
            if voto in OPCOES:
                votos.append(voto)
                break
            print("Voto invalido. Use: PLAYSTATION, XBOX ou NINTENDO.")

    contagem: Counter[str] = Counter(votos)
    maior = max(contagem.values())
    vencedores: list[str] = [console for console, qtd in contagem.items() if qtd == maior]

    print("\n--- RESULTADO FINAL ---")
    if len(vencedores) == 1:
        print(f"Console escolhido: {vencedores[0]}")
        print(f"Quantidade de votos: {maior}")
    else:
        print("Empate entre:", ", ".join(vencedores))
        print(f"Quantidade de votos: {maior}")


if __name__ == "__main__":
    main()
