from flask import Blueprint
from controllers.CommentController import *

CommentRoute = Blueprint("CommentRoute", __name__)

CommentRoute.route("/api/comments", methods=["POST"])(create_comment)
CommentRoute.route("/api/comments", methods=["GET"])(get_all_comments)
CommentRoute.route("/api/comments/<int:id>", methods=["DELETE"])(delete_comment_by_id)