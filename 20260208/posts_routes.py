from flask import request, jsonify
from flask_smorest import Blueprint,abort
from google.auth import message


def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description = "post api", url_prefix = "/posts")

    @posts_blp.route("/", methods = ["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()
        if request.method == "GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            post = cursor.fetchall()
            cursor.close()

            post_list = []
            for post in posts:
                post_list.append({
                    "id": post[0],
                    "title": post[1],
                    "content": post[2]
                })
            return jsonify(post_list)
        elif request.method == "POST":
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message = "Title or contents cannot be empty")
            sql = "INSERT INTO posts(title, content) VALUES (%s, %s)"
            cursor.execute(sql,(title,content))
            mysql.connection.commit()

            return jsonify({
                "msg": "success",
                "title": title,
                "content": content
            })

    @posts_blp.route("/<int:id>", methods = ["GET", "PUT", "DELETE"])
    def post(id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM posts WHERE id = {id}"
        cursor.execute(sql)
        post = cursor.fetchone()

        if request.method == "GET":
            if not post:
                abort(404, "Not found post")
            return ({"id": post[0],
                     "title": post[1],
                     "content": post[2]
                     })

        elif request.method == "PUT":
            title = request.json.get("title")
            content = request.json.get("content")

            if not post:
                abort(404, "not found")
            if not title or not content:
                abort(400, "Not found title, content")
            sql = f"UPDATE posts SET title = {title}, content = {content} WHERE id = {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return jsonify({"msg": "successfully update title & content"})

        elif request.method == "DELETE":
            if not post:
                abort(404, "Not found post")

            sql = f"DELETE FROM posts WHERE id = {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return jsonify({"msg": "success delete"})

    return posts_blp