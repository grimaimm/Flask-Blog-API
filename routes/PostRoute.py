from flask import Blueprint
from controllers.PostController import *

PostRoute = Blueprint("PostRoute", __name__)

PostRoute.route("/api/posts", methods=["POST"])(create_post)
PostRoute.route("/api/posts", methods=["GET"])(get_all_posts)
PostRoute.route("/api/posts/<int:id>", methods=["GET"])(get_post_by_id)
PostRoute.route("/api/posts/<int:id>", methods=["PUT"])(update_post_by_id)
PostRoute.route("/api/posts/<int:id>", methods=["DELETE"])(delete_post_by_id)
