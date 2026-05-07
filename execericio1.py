def acao_semafaro(cor: str):
    cor = cor.lower()
    if cor == 'vermelho': 
        return 'Pare'
    elif cor == 'amarelho':
        return 'Atenção'
    elif cor == 'verde':
        return 'Siga'
    return 'Cor inválida'