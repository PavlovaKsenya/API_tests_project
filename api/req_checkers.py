import json
import requests

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )

def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )

def code_ok(code):
    assert code == 200, "Response code is not 200(OK), but should be."

def code_created(code):
    assert code == 201, "Response code is not 201(CREATED), but should be."

def code_no_content(code):
    assert code == 204, "Response code is not 204(No Content), but should be."

def code_not_found(code):
    assert code == 404, "Response code is not 404(Not Found), but should be."

def code_bad_request(code):
    assert code == 400, "Response code is not 400(Bad request), but should be."

def request_get(url):
    return requests.get(url)

def request_post(url, headers, payload):
    return requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

def request_put(url, headers, payload):
    return requests.put(url, headers=headers, data=json.dumps(payload, indent=4))

def request_patch(url, headers, payload):
    return requests.patch(url, headers=headers, data=json.dumps(payload, indent=4))

def request_delete(url, headers, payload):
    return requests.delete(url, headers=headers, data=json.dumps(payload, indent=4))

def get_positive_resp(url):
    # convert dict to json string by json.dumps() for body data.
    resp = request_get(url)

    # Validate response headers and body contents, e.g. status code.
    code_ok(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def post_create_positive_resp(url, headers, payload):
    # convert dict to json string by json.dumps() for body data.
    resp = request_post(url, headers, payload)

    # Validate response headers and body contents, e.g. status code.
    code_created(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def post_positive_resp(url, headers, payload):
# convert dict to json string by json.dumps() for body data.
    resp = request_post(url, headers, payload)

    # Validate response headers and body contents, e.g. status code.
    code_ok(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def put_positive_resp(url, headers, payload):
    # convert dict to json string by json.dumps() for body data.
    resp = request_put(url, headers, payload)

    # Validate response headers and body contents, e.g. status code.
    code_ok(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def patch_positive_resp(url, headers, payload):
    # convert dict to json string by json.dumps() for body data.
    resp = request_patch(url, headers, payload)

    # Validate response headers and body contents, e.g. status code.
    code_ok(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def delete_positive_resp(url, headers, payload):
    # convert dict to json string by json.dumps() for body data.
    resp = request_delete(url, headers, payload)

    # Validate response headers and body contents, e.g. status code.
    code_no_content(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def get_negative_resp(url):
    # convert dict to json string by json.dumps() for body data.
    resp = request_get(url)

    # Validate response headers and body contents, e.g. status code.
    code_not_found(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)

def post_negative_resp(url, headers, payload):
    # convert dict to json string by json.dumps() for body data.
    resp = request_post(url, headers, payload)

    # Validate response headers and body contents, e.g. status code.
    code_bad_request(resp.status_code)

    # print full request and response
    pretty_print_request(resp.request)
    pretty_print_response(resp)