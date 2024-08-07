import sender_stand_request
import data


def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body


def get_new_user_autoken():
    new_user = sender_stand_request.post_new_user(data.user_body.copy())
    auth_token_value = new_user.json()["authToken"]
    new_user_autoken = data.headers.copy()
    new_user_autoken["Authorization"]= f"Bearer {auth_token_value}"
    return new_user_autoken


def positive_assert(kit_name): #PRUEBAS POSITIVAS

    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_autoken())

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name


def negative_assert(kit_name): #PRUEBAS NEGATIVAS
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_autoken())

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_create_kit_1_letter_in_kit_name_get_success_response(): #El número permitido de caracteres (1)
    positive_assert("A")


def test_create_kit_511_letters_in_kit_name_get_success_response(): #El número permitido de caracteres (511)
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                    dabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_zero_letters_in_kit_name_get_error_response(): #El num de caracteres es menor que la cantidad permitida(0)
    negative_assert("0")


def test_create_kit_512_letters_in_kit_name_get_error_response(): #El num de caracteres es > que la cantidad permitida (512)
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcD")


def test_create_kit_has_special_symbols_in_kit_name_get_success_response(): #Se permiten caracteres especiales
    positive_assert("№%@")


def test_create_kit_has_spaces_in_kit_name_get_success_response(): #Se permiten espacios
    positive_assert(" A Aaa ")


def test_create_kit_has_numbers_in_kit_name_get_success_response(): #Se permiten números
    positive_assert("123")


def test_create_kit_no_name_get_error_response(): #El parámetro no se pasa en la solicitud
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)


def test_create_kit_number_type_in_kit_name_get_error_response(): #Se ha pasado un tipo de parámetro diferente (número)
    negative_assert(123)
