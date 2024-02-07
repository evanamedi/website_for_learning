from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/topics")
def topics():
    return render_template("topics.html")



# OOP TOPICS
@app.route("/topics/oop")
def oop():
    return render_template("oop.html")

@app.route("/topics/oop/classes-and-objects")
def classes_and_objects():
    return render_template("classes-and-objects.html")

@app.route("/topics/oop/inheritance")
def inheritance():
    return render_template("inheritance.html")

@app.route("/topics/oop/encapsulation")
def encapsulation():
    return render_template("encapsulation.html")

@app.route("/topics/oop/polymorphism")
def polymorphism():
    return render_template("polymorphism.html")

@app.route("/topics/oop/abstraction")
def abstraction():
    return render_template("abstraction.html")

@app.route("/topics/oop/association")
def association():
    return render_template("association.html")

@app.route("/topics/oop/aggregation")
def aggregation():
    return render_template("aggregation.html")

@app.route("/topics/oop/composition")
def composition():
    return render_template("composition.html")

if __name__ == "__main__":
    app.run(debug=True)
