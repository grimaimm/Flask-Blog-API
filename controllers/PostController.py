from flask import jsonify, request
from config import db
from models.PostModel import Post
from models.CategoryModel import Category
from models.CommentModel import Comment
from models.AuthorModel import Author


# Method POST - Create Post - /api/posts
def create_post():
    new_post_data = request.get_json()

    author = Author.query.get(new_post_data.get("author_id"))
    if not author:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Gagal membuat post. Author tidak ditemukan",
                }
            ),
            404,
        )

    category = Category.query.get(new_post_data.get("category_id"))
    if not category:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Gagal membuat post. Category tidak ditemukan",
                }
            ),
            404,
        )

    new_post = Post(
        title=new_post_data["title"],
        content=new_post_data["content"],
        author_id=new_post_data["author_id"],
        category_id=new_post_data["category_id"],
    )
    db.session.add(new_post)

    author.total_posts = author.total_posts + 1
    db.session.add(author)

    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Post berhasil dibuat",
                "posts_data": new_post.to_dict(),
            }
        ),
        201,
    )


# Method GET - Get All Posts - /api/posts
def get_all_posts():
    posts = Post.query.all()
    posts_datas = []

    for post in posts:
        comments = Comment.query.filter_by(post_id=post.id).all()
        total_comments = len(comments)
        posts_data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated_at or "Belum ada update",
            "author_id": post.author_id,
            "author_name": post.author.name,
            "category_id": post.category_id,
            "category_name": post.category.name,
            "total_comments": total_comments,
        }
        posts_datas.append(posts_data)

    return jsonify({"status": "success", "posts_data": posts_datas}), 200


# Method GET - Get Post By ID - /api/posts/<int:id>
def get_post_by_id(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({"status": "error", "message": "Posts tidak ditemukan"}), 404

    comments = Comment.query.filter_by(post_id=post.id).all()
    total_comments = len(comments)
    comments_data = (
        [
            {
                "id": comment.id,
                "content": comment.content,
                "created_at": comment.created_at,
                "post_id": comment.post_id,
                "author_id": comment.author_id,
                "author_name": comment.author.name if comment.author else "Author tidak ditemukan"
            }
            for comment in comments
        ]
        if comments
        else "Tidak ada komentar yang ditemukan"
    )

    posts_data = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "created_at": post.created_at,
        "updated_at": post.updated_at or "Belum ada update",
        "author_id": post.author_id,
        "author_name": post.author.name,
        "category_id": post.category_id,
        "category_name": post.category.name,
        "total_comments": total_comments,
        "comments": comments_data,
    }
    return jsonify({"status": "success", "posts_data": posts_data}), 200


# Method PUT - Update Post By ID - /api/posts/<int:id>
def update_post_by_id(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({"status": "error", "message": "Posts tidak ditemukan"}), 404
    post_data = request.get_json()
    post.title = post_data["title"]
    post.content = post_data["content"]
    post.author_id = post_data["author_id"]
    post.category_id = post_data["category_id"]
    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Posts berhasil diperbarui",
                "posts_data": post.to_dict(),
            }
        ),
        200,
    )


# Method DELETE - Delete Post By ID - /api/posts/<int:id>
def delete_post_by_id(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({"status": "error", "message": "Posts tidak ditemukan"}), 404

    comments = Comment.query.filter_by(post_id=post.id).all()
    for comment in comments:
        db.session.delete(comment)

    author = Author.query.get(post.author_id)
    if author:
        author.total_posts = max(0, author.total_posts - 1)
        db.session.add(author)

    db.session.delete(post)
    db.session.commit()

    return (
        jsonify(
            {
                "status": "success",
                "message": f"Posts dengan ID {id} berhasil dihapus",
            }
        ),
        200,
    )