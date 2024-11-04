from config import app, db
from routes.AuthorRoute import AuthorRoute
from routes.CategoryRoute import CategoryRoute
from routes.CommentRoute import CommentRoute
from routes.PostRoute import PostRoute
from flask import jsonify

# Register Blueprints
app.register_blueprint(AuthorRoute)
app.register_blueprint(CategoryRoute)
app.register_blueprint(CommentRoute)
app.register_blueprint(PostRoute)


@app.route("/")
def index():
    api_list = {
        "Author APIs": {
            "1. Method POST - Membuat Authors": "/api/authors",
            "2. Method GET - Mengambil semua Authors": "/api/authors",
            "3. Method GET - Mengambil Author berdasarkan ID": "/api/authors/<id>",
            "4. Method PUT - Memperbarui Author berdasarkan ID": "/api/authors/<id>",
            "5. Method DELETE - Menghapus Author berdasarkan ID": "/api/authors/<id>",
        },
        "Category APIs": {
            "1. Method POST - Membuat Category": "/api/categories",
            "2. Method GET - Mengambil semua Category": "/api/categories",
            "3. Method DELETE - Menghapus Category berdasarkan ID": "/api/categories/<id>",
        },
        "Comment APIs": {
            "1. Method POST - Membuat Comment": "/api/comments",
            "2. Method GET - Mengambil semua Comment": "/api/comments",
            "3. Method DELETE - Menghapus Comment berdasarkan ID": "/api/comments/<id>",
        },
        "Post APIs": {
            "1. Method POST - Membuat Posts": "/api/posts",
            "2. Method GET - Mengambil semua Posts": "/api/posts",
            "3. Method GET - Mengambil Posts berdasarkan ID": "/api/posts/<id>",
            "4. Method PUT - Memperbarui Posts berdasarkan ID": "/api/posts/<id>",
            "5. Method DELETE - Menghapus Posts berdasarkan ID": "/api/posts/<id>",
        },
    }
    return jsonify({"status": "success", "available_apis": api_list}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5003, debug=True)
