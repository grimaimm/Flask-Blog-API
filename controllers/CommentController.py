from flask import jsonify, request
from config import db
from models.CommentModel import Comment
from models.PostModel import Post
from models.AuthorModel import Author


# Method POST - Create Comment - /api/comments
def create_comment():
    new_comment_data = request.get_json()

    post = Post.query.get(new_comment_data.get("post_id"))
    if not post:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Gagal membuat comment. Post tidak ditemukan",
                }
            ),
            404,
        )

    author = Author.query.get(new_comment_data.get("author_id"))
    if not author:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Gagal membuat comment. Author tidak ditemukan",
                }
            ),
            404,
        )

    new_comment = Comment(
        content=new_comment_data["content"],
        post_id=new_comment_data["post_id"],
        author_id=new_comment_data["author_id"],
    )
    db.session.add(new_comment)
    author.total_comments += 1
    db.session.add(author)

    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Comment berhasil ditambahkan.",
                "comments_data": new_comment.to_dict(),
            }
        ),
        201,
    )


# Method GET - Get All Comments - /api/comments
def get_all_comments():
    comments = Comment.query.all()
    comments_list = []

    for comment in comments:
        post = Post.query.get(comment.post_id)
        author = Author.query.get(comment.author_id)
        comment_data = {
            "id": comment.id,
            "content": comment.content,
            "created_at": comment.created_at,
            "post_id": comment.post_id,
            "post_title": post.title,
            "author_id": comment.author_id,
            "author_name": author.name,
        }
        comments_list.append(comment_data)
    return jsonify({"status": "success", "comments_data": comments_list}), 200


# Method DELETE - Delete Comment - /api/comments/:id
def delete_comment_by_id(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"status": "error", "message": "Comment tidak ditemukan."}), 404

    author = Author.query.get(comment.author_id)
    if author:
        if author.total_comments > 1:
            author.total_comments -= 1
        else:
            author.total_comments = 0

    db.session.delete(comment)
    db.session.commit()
    return (
        jsonify(
            {
                "status": "success",
                "message": "Comment dengan ID " + str(id) + " berhasil dihapus.",
            }
        ),
        200,
    )
