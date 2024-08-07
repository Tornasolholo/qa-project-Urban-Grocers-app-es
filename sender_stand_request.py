import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
'''response = get_docs()
print(response.status_code)'''


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_token)
