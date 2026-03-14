PACOTES: dict[str, dict] = {
    "1": {
        "nome": "Econômico",
        "categoria": "economica",
        "preco": 1500.00,
        "descricao": "Assento econômico, bagagem de mão inclusa.",
    },
    "2": {
        "nome": "Executivo",
        "categoria": "executiva",
        "preco": 3500.00,
        "descricao": "Assento executivo, bagagem despachada + refeição inclusa.",
    },
    "3": {
        "nome": "Primeira Classe",
        "categoria": "primeira",
        "preco": 8000.00,
        "descricao": "Assento primeira classe, serviço completo + lounge no aeroporto.",
    },
}

DESCONTOS: dict[str, dict[int, float]] = {
    "economica": {2: 0.03, 3: 0.04, 4: 0.05},
    "executiva":  {2: 0.05, 3: 0.07, 4: 0.08},
    "primeira":   {2: 0.10, 3: 0.15, 4: 0.20},
}


def exibir_pacotes() -> None:
    print("\n=== PACOTES DISPONÍVEIS ===")
    for chave, pacote in PACOTES.items():
        print(f"[{chave}] {pacote['nome']} — R$ {pacote['preco']:,.2f}")
        print(f"     {pacote['descricao']}")
    print()


def obter_percentual_desconto(categoria: str, quantidade_viajantes: int) -> float:
    if quantidade_viajantes < 2:
        return 0.0
    chave_quantidade = min(quantidade_viajantes, 4)
    return DESCONTOS[categoria][chave_quantidade]


def ler_pacote() -> dict:
    exibir_pacotes()
    while True:
        escolha = input("Escolha o pacote (1, 2 ou 3): ").strip()
        if escolha in PACOTES:
            return PACOTES[escolha]
        print("Opção invalida. Digite 1, 2 ou 3.")


def ler_quantidade_viajantes() -> int:
    while True:
        try:
            quantidade = int(input("Informe a quantidade de viajantes da mesma residencia: ").strip())
            if quantidade <= 0:
                print("Quantidade invalida. Digite um numero inteiro positivo.")
                continue
            return quantidade
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def main() -> None:
    pacote = ler_pacote()
    quantidade_viajantes = ler_quantidade_viajantes()

    valor_bruto = pacote["preco"] * quantidade_viajantes
    percentual_desconto = obter_percentual_desconto(pacote["categoria"], quantidade_viajantes)
    valor_desconto = valor_bruto * percentual_desconto
    valor_liquido = valor_bruto - valor_desconto
    valor_medio_por_viajante = valor_liquido / quantidade_viajantes

    print("\n--- RESUMO DA VIAGEM ---")
    print(f"Pacote escolhido:         {pacote['nome']}")
    print(f"Preco por viajante:       R$ {pacote['preco']:,.2f}")
    print(f"Quantidade de viajantes:  {quantidade_viajantes}")
    print(f"Valor bruto total:        R$ {valor_bruto:,.2f}")
    print(f"Desconto aplicado:        R$ {valor_desconto:,.2f} ({percentual_desconto * 100:.0f}%)")
    print(f"Valor liquido total:      R$ {valor_liquido:,.2f}")
    print(f"Valor medio por viajante: R$ {valor_medio_por_viajante:,.2f}")


if __name__ == "__main__":
    main()
