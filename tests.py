import unittest
from datetime import datetime, timedelta
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        john = User(username='john', email='john@example.com')
        susan = User(username='susan', email='susan@example.com')
        mary = User(username='mary', email='mary@example.com')
        david = User(username='david', email='david@example.com')
        db.session.add_all([john, susan, mary, david])

        # create four posts
        now = datetime.utcnow()
        post_john = Post(body="post from john", author=john,
            timestamp=now + timedelta(seconds=1))
        post_susan = Post(body="post from susan", author=susan,
            timestamp=now + timedelta(seconds=1))
        post_mary = Post(body="post from mary", author=mary,
            timestamp=now + timedelta(seconds=1))
        post_david = Post(body="post from david", author=david,
            timestamp=now + timedelta(seconds=1))
        db.session.add_all([post_john, post_susan, post_mary, post_david])
        db.session.commit()

        #set up the followers
        john.follow(susan)
        john.follow(david)
        susan.follow(mary)
        mary.follow(david)

        # check the followed posts of each author
        followed_by_john = john.followed_posts().all()
        followed_by_susan = susan.followed_posts().all()
        followed_by_mary = mary.followed_posts().all()
        followed_by_david = david.followed_posts().all()
        self.assertEqual(followed_by_john, [post_john, post_susan, post_david])
        self.assertEqual(followed_by_susan, [post_susan, post_mary])
        self.assertEqual(followed_by_mary, [post_mary, post_david])
        self.assertEqual(followed_by_david, [post_david])

if __name__ == '__main__':
    unittest.main(verbosity=2)
