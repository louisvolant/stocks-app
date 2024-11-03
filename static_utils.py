# app/static_utils.py

from functools import wraps
from flask import send_from_directory, make_response
import os

def add_static_route(app):
    def add_cache_headers(view_func):
        @wraps(view_func)
        def decorated_function(*args, **kwargs):
            response = view_func(*args, **kwargs)
            if isinstance(response, str):
                response = make_response(response)
            response.headers['Cache-Control'] = 'public, max-age=31536000'
            return response
        return decorated_function

    @app.route('/static/<path:filename>')
    @add_cache_headers
    def serve_static(filename):
        static_folder = os.path.abspath('./static')
        print(f"Serving static file: {filename} from {static_folder}")
        return send_from_directory(static_folder, filename)

    @app.route('/test-static')
    @add_cache_headers
    def test_static():
        print("Test static route called")
        return "Test static route"

    return app