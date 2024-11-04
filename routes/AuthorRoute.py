from flask import Blueprint
from controllers.AuthorController import *

AuthorRoute = Blueprint("AuthorRoute", __name__)

AuthorRoute.route("/api/authors", methods=["POST"])(create_author)
AuthorRoute.route("/api/authors", methods=["GET"])(get_all_authors)
AuthorRoute.route("/api/authors/<int:id>", methods=["GET"])(get_author_by_id)
AuthorRoute.route("/api/authors/<int:id>", methods=["PUT"])(update_author_by_id)
AuthorRoute.route("/api/authors/<int:id>", methods=["DELETE"])(delete_author_by_id)
