import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um determinado usuario no Github
    :param usuario: str com o nome de usuario do github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


