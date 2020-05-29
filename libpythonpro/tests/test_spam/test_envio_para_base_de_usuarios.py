import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Ernani', email='kakizon@gmail.com'),
            Usuario(nome='Nito', email='kakizon@gmail.com')
        ],
        [
            Usuario(nome='Ernani', email='kakizon@gmail.com')
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ernanidacosta@gmail.com',
        'Aula Python Pro',
        'Modulo PyTools'
    )
    assert len(usuarios) == enviador.quantidade_emails_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.quantidade_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.quantidade_emails_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Ernani', email='kakizon@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ernanidacosta@gmail.com',
        'Aula Python Pro',
        'Modulo PyTools'
    )
    assert enviador.parametros_de_envio == (
        'ernanidacosta@gmail.com',
        'kakizon@gmail.com',
        'Aula Python Pro',
        'Modulo PyTools'
    )