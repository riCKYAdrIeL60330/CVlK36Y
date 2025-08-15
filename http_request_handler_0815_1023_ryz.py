# 代码生成时间: 2025-08-15 10:23:48
import sys
import requests
def handle_http_request(url, method, data=None, headers=None):
    """
    Handle HTTP requests to a specified URL with provided method, data, and headers.
    
    Args:
        url (str): The URL to send the HTTP request to.
        method (str): The HTTP method to use (e.g., 'GET', 'POST', 'PUT', 'DELETE').
        data (dict or None): Data to be sent in the request body (for POST/PUT requests).
        headers (dict or None): Headers to include in the request.
        
    Returns:
        dict: A dictionary containing the HTTP response status code and content.
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data, headers=headers)
        elif method.upper() == 'PUT':
            response = requests.put(url, json=data, headers=headers)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            return {'error': 'Invalid HTTP method'}
        
        return {
            'status_code': response.status_code,
            'content': response.text
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    # Example usage: Send a GET request to https://jsonplaceholder.typicode.com/todos/1
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    method = 'GET'
    response = handle_http_request(url, method)
    print(response)