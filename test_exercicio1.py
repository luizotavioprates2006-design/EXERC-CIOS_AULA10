from execericio1 import acao_semafaro

def  test_cor_vermelho():
    assert acao_semafaro('vermelho') == 'Pare'

def test_cor_amarelo():
    assert acao_semafaro('amarelho') == 'Atenção'

def test_cor_verde():
    assert acao_semafaro('verde') == 'Siga'

def teste_cor_errada():
    assert acao_semafaro('rosa') == 'Cor inválida'