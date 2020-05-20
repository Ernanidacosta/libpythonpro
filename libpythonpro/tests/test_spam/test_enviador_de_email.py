import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['ernanidacosta@gmail.com', 'foo@bar.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'kakizon@gmail.com',
        'Cursos Python Pro',
        'Primeira Turma Aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)

def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'kakizon@gmail.com',
            'Cursos Python Pro',
            'Primeira Turma Aberta'
        )


