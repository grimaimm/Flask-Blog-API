from flask import Blueprint
from controllers.CategoryController import *

CategoryRoute = Blueprint("CategoryRoute", __name__)

CategoryRoute.route("/api/categories", methods=["POST"])(create_category)
CategoryRoute.route("/api/categories", methods=["GET"])(get_all_categories)
CategoryRoute.route("/api/categories/<int:id>", methods=["DELETE"])(delete_category_by_id)