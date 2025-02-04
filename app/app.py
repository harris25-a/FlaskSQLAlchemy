from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# app.secret_key = '12'
#
# # Configure Database
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


# Define User Model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(25), unique=True, nullable=False)
#     password_hash = db.Column(db.String(150), nullable=False)
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
# # Initialize Database
# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    # if "username" in session:
    #     return redirect(url_for("book_page"))
    return render_template("home.html")


# # Login Route
@app.route("/login", methods=["GET", "POST"])
def login_page():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#
#         user = User.query.filter_by(username=username).first()
#         if user and user.check_password(password):
#             session['username'] = username
#             return redirect(url_for("book_page"))
#
#         return render_template("login.html", error="Invalid credentials")
#
    return render_template("login.html")
#
#
# Register Route
@app.route("/register", methods=["GET", "POST"])
def register_page():
    # if request.method == "POST":
    #     username = request.form.get("username")
    #     password = request.form.get("password")
    #
    #     if not username or not password:
    #         return render_template("login.html", error="All fields are required")
    #
    #     user = User.query.filter_by(username=username).first()
    #     if user:
    #         return render_template("login.html", error="Username already registered")
    #
    #     new_user = User(username=username)
    #     new_user.set_password(password)
    #
    #     db.session.add(new_user)
    #     db.session.commit()
    #
    #     session['username'] = username
    #     return redirect(url_for("book_page"))

    return render_template("login.html")


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/visit")
def visit_page():
    return render_template("visit.html")




@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/plan")
def plan_page():
    return render_template("plan.html")


@app.route("/book")
def book_page():
    # if "username" in session:
    #     return render_template("book.html", username=session["username"])
    return render_template("book.html")


if __name__ == "__main__":
    app.run(debug=True)
