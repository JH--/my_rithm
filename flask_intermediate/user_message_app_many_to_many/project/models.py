from project import db

UserMessages = db.Table(
    "user_messages",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id", ondelete="cascade")),
    db.Column(
        "message_id", db.Integer, db.ForeignKey("messages.id", ondelete="cascade")
    ),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship(
        "Message", secondary=UserMessages, backref=db.backref("users")
    )

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)

    def __init__(self, message):
        self.message = message
