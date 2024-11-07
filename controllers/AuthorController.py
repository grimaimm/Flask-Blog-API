from flask import jsonify, request
from config import db
from models.AuthorModel import Author
from models.PostModel import Post
from models.CommentModel import Comment


# Method POST - Create Author - /api/authors
def create_author():
    new_author_data = request.get_json()
    new_author = Author(
        name=new_author_data["name"],
        email=new_author_data["email"],
    )
    db.session.add(new_author)
    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Author berhasil dibuat",
                "authors_data": new_author.to_dict(),
            }
        ),
        201,
    )


# Method GET - Get all authors - /api/authors
def get_all_authors():
    authors = Author.query.all()
    authors_lists = []

    for author in authors:
        authors_list = {
            "id": author.id,
            "name": author.name,
            "email": author.email,
            "total_posts": author.total_posts,
            "total_comments": author.total_comments,
        }

        authors_lists.append(authors_list)

    return jsonify({"status": "success", "authors_data": authors_lists}), 200


# Method GET - Get author by id - /api/authors/:id
def get_author_by_id(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({"status": "error", "message": "Author tidak ditemukan"}), 404

    posts = Post.query.filter_by(author_id=author.id).all()
    comments = Comment.query.filter_by(author_id=author.id).all()

    posts_data = (
        [
            {
                "id": post.id,
                "title": post.title,
                "created_at": post.created_at,
            }
            for post in posts
        ]
        if posts
        else "Tidak ada postingan yang ditemukan"
    )

    comments_data = (
        [
            {
                "id": comment.id,
                "content": comment.content,
                "created_at": comment.created_at,
                "post_id": comment.post_id,
            }
            for comment in comments
        ]
        if comments
        else "Tidak ada komentar yang ditemukan"
    )

    author_data = {
        "id": author.id,
        "name": author.name,
        "email": author.email,
        "total_posts": author.total_posts,
        "total_comments": author.total_comments,
        "posts": posts_data,
        "comments": comments_data,
    }

    return jsonify({"status": "success", "authors_data": author_data}), 200


# Method PUT - Update author by id - /api/authors/:id
def update_author_by_id(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({"status": "error", "message": "Author tidak ditemukan"}), 404
    author_data = request.get_json()
    author.name = author_data["name"]
    author.email = author_data["email"]
    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Author berhasil diperbarui",
                "authors_data": author.to_dict(),
            }
        ),
        200,
    )


# Method DELETE - Delete author by id - /api/authors/:id
def delete_author_by_id(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({"status": "error", "message": "Author tidak ditemukan"}), 404

    posts = Post.query.filter_by(author_id=author.id).all()
    if posts:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Author tidak bisa dihapus karena masih memiliki postingan",
                }
            ),
            400,
        )

    comments = Comment.query.filter_by(author_id=author.id).all()
    for comment in comments:
        db.session.delete(comment)

    db.session.delete(author)
    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Author dengan ID " + str(id) + " berhasil dihapus",
            }
        ),
        200,
    )
