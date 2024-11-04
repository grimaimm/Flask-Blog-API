from flask import jsonify, request
from config import db
from models.CategoryModel import Category
from models.PostModel import Post
from models.AuthorModel import Author


# Method POST - Create Category - /api/categories
def create_category():
    new_category_data = request.get_json()
    new_category = Category(name=new_category_data["name"])
    db.session.add(new_category)
    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Category berhasil dibuat",
                "categories_data": new_category.to_dict(),
            }
        ),
        201,
    )


# Method GET - Get All Categories - /api/categories
def get_all_categories():
    categories = Category.query.all()
    categories_list = []

    for category in categories:
        total_posts = len(category.posts)
        category_data = {
            "id": category.id,
            "name": category.name,
            "total_posts": total_posts if total_posts else 0,
        }
        categories_list.append(category_data)
    return jsonify({"status": "success", "categories_data": categories_list}), 200


# Method DELETE - Delete Category By ID - /api/categories/<int:id>
def delete_category_by_id(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"status": "error", "message": "Category tidak ditemukan"}), 404

    posts = Post.query.filter_by(category_id=category.id).all()
    for post in posts:
        author = Author.query.get(post.author_id)
        if author:
            author.total_posts -= 1
            db.session.add(author)

        db.session.delete(post)

    db.session.delete(category)
    db.session.commit()
    return jsonify(
        {
            "status": "success",
            "message": "Category dengan ID " + str(id) + " berhasil dihapus.",
        }
    )
