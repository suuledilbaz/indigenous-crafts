from flask import Flask, render_template, request, jsonify

from models import db, User, Craft

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///indigenous_crafts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def home():
    return "RUNNING YAY"

@app.route("/register", methods=["GET", "POST"])
def register():



    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "This email is already registered."


        new_user = User(
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return "Registration successful!"

    return render_template("register.html")
    
@app.route("/login", methods=["GET", "POST"])       

def login(): 
    
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user is None:
            return "User not found."

        if user.password != password:
            return "Incorrect password."

        return "Login successful!"

    return render_template("login.html")

@app.route("/create_craft", methods=["GET", "POST"])
def create_craft():
    if request.method == "POST":
        name = request.form["name"]
        craft_type = request.form["craft_type"]
        location = request.form["location"]
        description = request.form["description"]
        material = request.form["material"]
        production_method = request.form["production_method"]
        story = request.form["story"]
        cultural_information = request.form["cultural_information"]
        pattern = request.form["pattern"]

        user = User.query.first()

        new_craft = Craft(
            name=name,
            craft_type=craft_type,
            location=location,
            description=description,
            material=material,
            production_method=production_method,
            story=story,
            cultural_information=cultural_information,
            pattern=pattern,
            user_id=user.id
        )

        db.session.add(new_craft)
        db.session.commit()

        return "Craft created successfully!"

    return render_template("create_craft.html")

@app.route("/crafts")
def crafts():
    search_query = request.args.get("q", "").strip()
    if search_query:
        all_crafts = Craft.query.filter(Craft.name.ilike(f"%{search_query}%")).all()
    else:
        all_crafts = Craft.query.all()
    return render_template("crafts.html", crafts=all_crafts)

@app.route("/craft_detail/<int:craft_id>")
def craft_detail(craft_id):
    craft = Craft.query.get_or_404(craft_id)
    return render_template("craft_detail.html", craft=craft)