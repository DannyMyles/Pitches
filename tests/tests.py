import unittest
from app.models import User,Pitch,Comment
from app import db

def setUp(self):
    '''
    Sets up the tests to be tested 
    '''
    self.Danny = User(username = 'Danny',password = 'passtest', email = 'test@test.com')
    self.pitch_one = Pitch(pitch = 'buy',category = 'Goods',user = self.Danny)
    self.new_comment = Comment(comment = 'feels good',pitch = self.pitch_one,user = 'Danny')


def tearDown(self):
    '''
    Tears down the values after every test
    '''
    Pitch.query.delete()
    User.query.delete()
    Comment.query.delete()

def test_check_instance_variables(self):
    '''
    Tests the instances of comment
    '''
    self.assertEquals(self.pitch_one.pitch,'feels good')
    self.assertEquals(self.pitch_one.category,'Goods')
    self.assertEquals(self.pitch_one.user,self.Danny)

def test_instance_of_comment(self):
    '''
    test comment of instances
    '''
    self.assertEquals(self.new_comment.comment,'feels good')
    self.assertEquals(self.new_comment.pitch,self.pitch_one)
    self.assertEquals(self.new_comment.user,self.Danny)

def test_save_picth(self):
    self.pitch_one.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)