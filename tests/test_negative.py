from api.req_checkers import get_negative_resp, post_negative_resp


def test_get_not_found_single_resourse():
    url = "https://reqres.in/api/unknown/23"

    get_negative_resp(url)

def test_get_not_found_single_user():
    url = "https://reqres.in/api/users/23"

    get_negative_resp(url)

def test_post_register_unsuccessfel():
    url = 'https://reqres.in/api/register'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {"email": "sydney@fife"}

    post_negative_resp(url, headers, payload)

def test_post_login_unsuccessfel():
    url = "https://reqres.in/api/login"

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {"email": "peter@klaven"}

    post_negative_resp(url, headers, payload)