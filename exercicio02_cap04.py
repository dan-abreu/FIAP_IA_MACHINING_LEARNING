def normalizar_categoria(texto: str) -> str:
    valor = texto.strip().lower()

    if valor in {"economica", "econômica", "e"}:
        return "economica"
    if valor in {"executiva", "x"}:
        return "executiva"
    if valor in {"primeira classe", "primeira", "p"}:
        return "primeira"

    raise ValueError("Categoria invalida. Use: economica, executiva ou primeira classe.")


def obter_percentual_desconto(categoria: str, quantidade_viajantes: int) -> float:
    if quantidade_viajantes < 2:
        return 0.0

    descontos = {
        "economica": {2: 0.03, 3: 0.04, 4: 0.05},
        "executiva": {2: 0.05, 3: 0.07, 4: 0.08},
        "primeira": {2: 0.10, 3: 0.15, 4: 0.20},
    }

    chave_quantidade = quantidade_viajantes if quantidade_viajantes <= 3 else 4
    return descontos[categoria][chave_quantidade]


def ler_valor_bruto() -> float:
    while True:
        try:
            valor = float(input("Informe o valor bruto do pacote (R$): ").strip().replace(",", "."))
            if valor <= 0:
                print("Valor invalido. Digite um numero maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada invalida. Digite apenas numeros.")


def ler_categoria() -> str:
    while True:
        try:
            texto = input("Informe a categoria dos assentos (economica, executiva, primeira classe): ")
            return normalizar_categoria(texto)
        except ValueError as erro:
            print(erro)


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
    valor_bruto = ler_valor_bruto()
    categoria = ler_categoria()
    quantidade_viajantes = ler_quantidade_viajantes()

    percentual_desconto = obter_percentual_desconto(categoria, quantidade_viajantes)
    valor_desconto = valor_bruto * percentual_desconto
    valor_liquido = valor_bruto - valor_desconto
    valor_medio_por_viajante = valor_liquido / quantidade_viajantes

    print("\n--- RESUMO DA VIAGEM ---")
    print(f"Valor bruto da viagem: R$ {valor_bruto:.2f}")
    print(f"Valor do desconto: R$ {valor_desconto:.2f} ({percentual_desconto * 100:.0f}%)")
    print(f"Valor liquido da viagem: R$ {valor_liquido:.2f}")
    print(f"Valor medio por viajante: R$ {valor_medio_por_viajante:.2f}")


if __name__ == "__main__":
    main()
