from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    S_name = models.CharField(max_length=100)
    S_code = models.CharField(max_length=7)
    S_collage = models.CharField(max_length=100)
    S_level = models.CharField(max_length=7)


class Cource(models.Model):
    Subject = models.ForeignKey(Subject)
    C_title = models.CharField(max_length=100)
    C_descrbtion = models.TextField(max_length=1000)
    C_pupdate = models.DateTimeField(auto_now_add=True)
    C_location = models.TextField(max_length=1000)
    def __unicode__(self):
        return self.C_title + "-" +self.user


class Lecture(models.Model):
    Cources = models.ForeignKey(Cource)
    L_title = models.CharField(max_length=100)
    L_sorces = models.TextField(max_length=500)
    L_objectives = models.TextField(max_length=500)
    L_pupdate = models.DateTimeField(auto_now_add=True)
    L_link = models.URLField()
    def __unicode__(self):
        return self.L_title + "-" +self.user


class View(models.Model):
    Lecture = models.ForeignKey(Lecture)
    pass


class Evaluation(models.Model):
    pass


class Comment(models.Model):
    Cource = models.ForeignKey(Cource)
    Lecture = models.ForeignKey(Lecture)
    C_auther = models.CharField(max_length=50)
    body = models.TextField()
    pup_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if Comment in Cource:
            return self.Cource + "-" +self.user
        if Comment in Lecture:
            return self.Lecture + "-" +self.user