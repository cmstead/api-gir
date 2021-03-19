from .config import get_config
from flask import Flask, request
app = Flask(__name__)


def run_server():
    config = get_config()

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def route_to_lambda(path):
        lambdas = [definition for definition in config["lambdas"] \
            if definition["name"].lower() == path.lower()]

        if len(lambdas) > 0:
            request_data = request.get_json()
            return f"You visited {str(config)}"
        else:
            return "not found", 404

    app.run()


if __name__ == "__main__":
    run_server()
