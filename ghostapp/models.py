from django.db import models
from django.utils.timezone import now


# Create your models here.
class BoastRoast(models.Model):#helped by Sohail
    body = models.CharField(max_length=280)
    boast_roast = models.BooleanField()
    upvote = models.IntegerField(default=0,null=True)
    downvote = models.IntegerField(default=0, null=True)
    timestamp = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.body
    
    @property
    def totalvotes(self):
        return self.upvote + self.downvote


