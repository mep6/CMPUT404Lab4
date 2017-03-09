import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


#makemigrations - responsible for creating new migrations based on the changes to the models
#migrate - applys and unapplys migrations
#> sqlite3 db.sqlite3 <--command to get into the db
#> .tables <--command in DB to see tables 

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text