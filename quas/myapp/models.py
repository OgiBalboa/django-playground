from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class SaveGame(models.Model):
    save_date = models.DateTimeField()
    top_score = models.IntegerField(default=0)
    player_name = models.CharField(max_length=50,default = "guest")
    def __str__(self):
        return self.player_name

    def update_score(self,score,time):
        return self.top_score > score