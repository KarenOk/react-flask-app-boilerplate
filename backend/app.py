from flask import Flask, jsonify
from flask_cors import CORS

from models import db, setup_db


def create_app():
    app = Flask(__name__)
    # setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        """ 
            Set access control headers
        """

        response.headers.add("Access-Control-Allow-Headers",
                             "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods",
                             "GET, POST, PATCH, DELETE, OPTIONS")

        return response

    @app.route("/")
    def index():
        """
            Health Check
        """

        return "This API is up and running"

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Your request was not formatted properly."
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "The requested respource was not found."
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed."
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Something went wrong on our end."
        }), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
