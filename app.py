from config import app, db
from routes.AuthorRoute import AuthorRoute
from routes.CategoryRoute import CategoryRoute
from routes.CommentRoute import CommentRoute
from routes.PostRoute import PostRoute

# Register Blueprints
app.register_blueprint(AuthorRoute)
app.register_blueprint(CategoryRoute)
app.register_blueprint(CommentRoute)
app.register_blueprint(PostRoute)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5003, debug=True)
