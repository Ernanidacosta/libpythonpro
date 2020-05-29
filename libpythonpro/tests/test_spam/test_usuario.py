from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Ernani', email='kakizon@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='Ernani', email='kakizon@gmail.com'), Usuario(nome='Nito', email='kakizon@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
