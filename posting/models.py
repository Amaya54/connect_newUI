from django.db import models

# Create your models here.
class postDetails(models.Model):
    postId = models.CharField(max_length=200,primary_key=True)
    title = models.CharField(max_length=200)
    userId = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    dop = models.DateTimeField(auto_now_add=True)
    filterBy = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)


    def makeJson(self):
        return {
            'postId': self.postId,
            'title': self.title,
            'content': self.content,
            'dop': self.dop,
            'userId':self.userId,
            'filterBy': self.filterBy,
            'tags': self.tags
        }