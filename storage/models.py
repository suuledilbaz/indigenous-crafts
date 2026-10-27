
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


craft_tags = db.Table(
    "craft_tags",
    db.Column(
        "craft_id",
        db.Integer,
        db.ForeignKey("craft.id"),
        primary_key=True
    ),
    db.Column(
        "tag_id",
        db.Integer,
        db.ForeignKey("tag.id"),
        primary_key=True
    )
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text, nullable=True)


class Craft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    craft_type = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    material = db.Column(db.String(120), nullable=True)
    production_method = db.Column(db.Text, nullable=True)
    story = db.Column(db.Text, nullable=True)
    cultural_information = db.Column(db.Text, nullable=True)
    pattern = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(200), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    tags = db.relationship(
        "Tag",
        secondary=craft_tags,
        backref="crafts"
    )

    measurements = db.relationship(
        "Measurement",
        backref="craft",
        cascade="all, delete-orphan"
    )

    images = db.relationship(
        "CraftImage",
        backref="craft",
        cascade="all, delete-orphan"
    )


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(50), nullable=False)

    craft_id = db.Column(
        db.Integer,
        db.ForeignKey("craft.id"),
        nullable=False
    )


class CraftImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(500), nullable=False)

    craft_id = db.Column(
        db.Integer,
        db.ForeignKey("craft.id"),
        nullable=False
    )