import unittest
from app.models import Comment, User
from app import db

def setUp(self):
    self.user_allan = User(username='Allan', password='lit',email='allan@gmail.com')
    self.new_comment = Comment(post_id=12,comment='Wagwan', user=self.user_allan)


def tearDown(self):
    Comment.query.delete()
    User.query.delete()


def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.post_id,12)
    self.assertEquals(self.new_comment.comment,'Wagwan')
    self.assertEquals(self.new_comment.user,self.user_allan)


def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12)
        self.assertTrue(len(got_comments) == 1)


if __name__ == '__main__':
    unittest.main()