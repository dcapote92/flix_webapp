import requests


class Auth:

    def __init__(self):
        self.__base_url = 'https://dcapote92.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.base_url}authentication/token/'

    def get_token(self, user: str, password: str) -> str:

        auth_payload = {
            'user': user,
            'password': password
        }

        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )

        if auth_payload.status_code == 200:
            return auth_response.json()

        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}
