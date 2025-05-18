"""
função de validação do cartão de crédito inserido pelo usuário
"""
def validar_cartao(numero_cartao): 
    numero_cartao = numero_cartao.replace(" ", "").replace("-", "") # removendo espaços e traços do número do cartão
    
    if not numero_cartao.isdigit() or len(numero_cartao) < 13 or len(numero_cartao) > 19:
        return "Número de cartão inválido. Deve conter entre 13 e 19 dígitos."

    # Algoritmo de Luhn para validação 
    soma = 0
    alternar = False
    for digito in reversed(numero_cartao):
        d = int(digito)
        if alternar:
            d *= 2
            if d > 9:
                d -= 9
        soma += d
        alternar = not alternar

    if soma % 10 != 0:
        return "Número de cartão inválido."

    # Identificação da bandeira conforme critério em data > base.png
    if numero_cartao.startswith(("34", "37")):
        return "Bandeira: American Express"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        return "Bandeira: MasterCard"
    elif numero_cartao.startswith("4"):
        return "Bandeira: Visa"
    elif numero_cartao.startswith("6011") or numero_cartao.startswith("65"):
        return "Bandeira: Discover"
    else:
        return "Bandeira desconhecida."