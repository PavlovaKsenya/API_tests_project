from api.req_checkers import get_positive_resp, post_create_positive_resp, post_positive_resp, put_positive_resp, \
    patch_positive_resp, delete_positive_resp


def test_get_list_resourses():
    url = "https://reqres.in/api/unknown"
    get_positive_resp(url)

def test_get_single_resourse():
    url = "https://reqres.in/api/unknown/2"
    get_positive_resp(url)

def test_get_list_users():
    url = "https://reqres.in/api/users?page=2"
    get_positive_resp(url)

def test_get_single_user():
    url = "https://reqres.in/api/users/2"
    get_positive_resp(url)

def test_post_create_user():
    url = 'https://reqres.in/api/users'
    # Additional headers.
    headers = {'Content-Type': 'application/json'}
    # Body
    payload = {"name": "morpheus", "job": "leader"}
    post_create_positive_resp(url, headers, payload)

def test_put_update_user():
    url = 'https://reqres.in/api/users/2'
    # Additional headers.
    headers = {'Content-Type': 'application/json'}
    # Body
    payload = {"name": "morpheus", "job": "zion resident"}
    put_positive_resp(url, headers, payload)

def test_patch_update_user():
    url = 'https://reqres.in/api/users/2'
    # Additional headers.
    headers = {'Content-Type': 'application/json'}
    # Body
    payload = {"name": "morpheus", "job": "zion resident"}
    patch_positive_resp(url, headers, payload)

def test_delete_user():
    url = 'https://reqres.in/api/users/2'
    # Additional headers.
    headers = {}
    # Body
    payload = {}
    delete_positive_resp(url, headers, payload)

def test_post_register_successfel():
    url = 'https://reqres.in/api/register'
    # Additional headers.
    headers = {'Content-Type': 'application/json'}
    # Body
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    post_positive_resp(url, headers, payload)

def test_post_login_successfel():
    url = 'https://reqres.in/api/login'
    # Additional headers.
    headers = {'Content-Type': 'application/json'}
    # Body
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    post_positive_resp(url, headers, payload)

def test_get_delayed_response():
    url = "https://reqres.in/api/users?delay=3"
    get_positive_resp(url)