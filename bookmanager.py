import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Book(db.Model):
    title =db.column(db.String(80), unique=True, nullable=False, primary_key=True)
    authorname =db.column(db.string, unique=True, nullable=False, Primary_key=True)
    publisher =db.column(db.string(80) ,unique=True, nullable=False, Primary_key=True)
    index =db.column(db.string(150) ,unique=True, nullable=False, Primary_key=True)

    def __repr__(self,title, authorname, publisher, index):
        return "<Title: {}>","<authorname: {}>" ,"<publisher: {}>", "<index: {}>".format(self.title,self.authorname,self.publisher,self.index)


@app.route("/" ,methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            authorname =Authorname

            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=8087, debug=True)







