from project import db, bcrypt

UserMessages = db.Table(
    "user_messages",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id", ondelete="cascade")),
    db.Column(
        "message_id", db.Integer, db.ForeignKey("messages.id", ondelete="cascade")
    ),
)

MessageTags = db.Table(
    "message_tags",
    db.Column("id", db.Integer, primary_key=True),
    db.Column(
        "message_id", db.Integer, db.ForeignKey("messages.id", ondelete="cascade")
    ),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id", ondelete="cascade")),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship(
        "Message", secondary=UserMessages, backref=db.backref("users")
    )

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode("UTF-8")

    @classmethod
    def authenticate(cls, username, password):
        found_user = cls.query.filter_by(username=username).first()
        if found_user:
            is_authenticated = bcrypt.check_password_hash(found_user.password, password)
            if is_authenticated:
                return found_user
        return False


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)

    def __init__(self, message):
        self.message = message


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Text)
    messages = db.relationship(
        "Message", secondary=MessageTags, backref=db.backref("tags")
    )

    def __init__(self, tag):
        self.tag = tag
