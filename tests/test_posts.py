import unittest
from app import create_app, db
from app.posts.models import Post

class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.post = Post(title="Test Post", body="Test Body", category="tech", author="Tester")
        db.session.add(self.post)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.client.get("/post")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Post", response.data)

    def test_create_post(self):
        response = self.client.post("/post/create", data={
            "title": "New Post",
            "body": "This is the body",
            "category": "tech",
            "author": "Author Name"
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"New Post", response.data)

        post = db.session.query(Post).filter_by(title="New Post").first()
        self.assertIsNotNone(post)
        self.assertEqual(post.body, "This is the body")

    def test_show_post(self):
        response = self.client.get(f"/post/{self.post.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Post", response.data)
        self.assertIn(b"Test Body", response.data)

    def test_edit_post(self):
        response = self.client.post(f"/post/edit/{self.post.id}", data={
            "title": "Edited Post",
            "body": "Edited Body",
            "category": "tech",
            "author": "Editor"
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        updated_post = db.session.get(Post, self.post.id)
        self.assertEqual(updated_post.title, "Edited Post")
        self.assertEqual(updated_post.body, "Edited Body")
        self.assertEqual(updated_post.author, "Editor")

    def test_delete_post(self):
        response = self.client.post(f"/post/delete/{self.post.id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        deleted_post = db.session.get(Post, self.post.id)
        self.assertIsNone(deleted_post)

if __name__ == '__main__':
    unittest.main()
