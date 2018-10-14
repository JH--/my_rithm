from app import app, db, User, Message
from flask_testing import TestCase
import unittest


class BaseTestCase(TestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"
        return app

    def setUp(self):
        db.create_all()
        user1 = User("Steph", "Curry")
        user2 = User("Klay", "Thompson")
        user3 = User("Draymond", "Green")
        message1 = Message("Splash!", 1)
        message2 = Message("My dog's name is Rocco", 2)
        message3 = Message("Dre day all day", 3)
        db.session.add_all([user1, user2, user3])
        db.session.add_all([message1, message2, message3])
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_index(self):
        response = self.client.get("/messages", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Splash!", response.data)
        self.assertIn(b"Dre day all day", response.data)
        self.assertIn(b"Steph Curry", response.data)
        self.assertIn(b"Draymond Green", response.data)

    def test_index_redirect(self):
        response = self.client.get("/", content_type="html/text", follow_redirects=True)
        self.assertIn(b"Splash!", response.data)

    def test_show_all_users(self):
        response = self.client.get("/users", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Steph Curry", response.data)
        self.assertIn(b"Draymond Green", response.data)

    def test_show_user(self):
        response = self.client.get("/users/1", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Steph Curry", response.data)

    def test_show_message(self):
        response = self.client.get("/messages/1", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(
            "/users",
            data=dict(first_name="new", last_name="student"),
            follow_redirects=True,
        )
        self.assertIn(b"new student", response.data)

    def test_create_message(self):
        response = self.client.post(
            "/messages/1",
            data=dict(message="new message", user_id=1),
            follow_redirects=True,
        )
        self.assertIn(b"new message", response.data)

    def test_edit_user(self):
        response = self.client.get("/users/1/edit")
        self.assertIn(b"Steph", response.data)
        self.assertIn(b"Curry", response.data)

    def test_edit_message(self):
        response = self.client.get("/messages/1/edit")
        self.assertIn(b"Splash!", response.data)

    def test_update_user(self):
        response = self.client.patch(
            "/users/1",
            data=dict(first_name="updated", last_name="information"),
            follow_redirects=True,
        )
        self.assertIn(b"updated information", response.data)
        self.assertNotIn(b"Steph Curry", response.data)

    def test_update_message(self):
        response = self.client.patch(
            "/messages/3",
            data=dict(message="updated message", user_id=3),
            follow_redirects=True,
        )
        self.assertIn(b"updated message", response.data)
        self.assertNotIn(b"Dre day", response.data)

    def test_delete_user(self):
        response = self.client.delete("/users/2", follow_redirects=True)
        self.assertNotIn(b"Klay Thompson", response.data)

    def test_delete_message(self):
        response = self.client.delete("/messages/1", follow_redirects=True)
        self.assertNotIn(b"Splash!", response.data)

    def test_empty_user(self):
        response = self.client.post(
            "/users",
            data=dict(first_name=" ", last_name="student"),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.post(
            "/users",
            data=dict(first_name="", last_name="student"),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.post(
            "/users",
            data=dict(first_name="student", last_name=" "),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.post(
            "/users",
            data=dict(first_name="student", last_name=""),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.patch(
            "/users/1",
            data=dict(first_name="student", last_name=" "),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.patch(
            "/users/1",
            data=dict(first_name="student", last_name=""),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.patch(
            "/users/1",
            data=dict(first_name="", last_name="student"),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)
        response = self.client.patch(
            "/users/1",
            data=dict(first_name=" ", last_name="student"),
            follow_redirects=True,
        )
        self.assertNotIn(b"student", response.data)

    def test_empty_message(self):
        response = self.client.post(
            "/messages/1",
            data=dict(message="", user_id=23),
            follow_redirects=True,
        )
        self.assertNotIn(b"23", response.data)
        response = self.client.post(
            "/messages/1",
            data=dict(message=" ", user_id=23),
            follow_redirects=True,
        )
        self.assertNotIn(b"23", response.data)


if __name__ == "__main__":
    unittest.main()
