from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'ernanidacosta', 'id': 11460643,
        'avater_url': 'https://avatars3.githubusercontent.com/u/11460643?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('ernanidacosta ')
    assert 'https://avatars3.githubusercontent.com/u/11460643?v=4' == url