# Python imports
from decimal import Decimal
from enum import Enum
from typing import Optional

# Pip imports

from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, null=True)
    password = fields.CharField(max_length=255)

class Quiz(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255, null=True)
    category = fields.ForeignKeyField("models.Category")
    difficulty = fields.CharField(max_length=255)
    owner = fields.ForeignKeyField('models.User')

class Question(models.Model):
    id = fields.IntField(pk=True)
    question_text = fields.CharField(max_length=255)
    options = fields.TextField()
    correct_answer = fields.CharField(max_length=255)
    quiz = fields.ForeignKeyField('models.Quiz')

class Answer(models.Model):
    id = fields.IntField(pk=True)
    answer = fields.CharField(max_length=255)
    question = fields.ForeignKeyField('models.Question', related_name="answer")
    user = fields.ForeignKeyField('models.User', related_name="answer")

class Result(models.Model):
    id = fields.IntField(pk=True)
    score = fields.IntField()
    time_taken = fields.CharField(max_length=255)
    user = fields.ForeignKeyField('models.User')
    quiz = fields.ForeignKeyField('models.Quiz')

class Category(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

class Session(models.Model):
    id = fields.IntField(pk=True)
    start_time = fields.CharField(max_length=255)
    end_time = fields.CharField(max_length=255)
    user = fields.ForeignKeyField('models.User')

class Feedback(models.Model):
    id = fields.IntField(pk=True)
    feedback_text = fields.CharField(max_length=255)
    user = fields.ForeignKeyField('models.User')
