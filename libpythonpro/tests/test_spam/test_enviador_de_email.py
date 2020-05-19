from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'ernanidacosta@gmail.com',
        'kakizon@gmail.com',
        'Cursos Python Pro',
        'Primeira Turma Aberta'
    )
    assert 'ernanidacosta@gmail.com' in resultado