from flask import Blueprint, request, current_app, jsonify
from src.app.flask.controllers.create_user_controller \
    import CreateUserController


blueprint_create_user = Blueprint("create_user", __name__)


@blueprint_create_user.route("/user/", methods=["POST"])
def create_user_blueprint():
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = CreateUserController(logger)
    result = controller.execute(input_json)
    return jsonify(result), 201
