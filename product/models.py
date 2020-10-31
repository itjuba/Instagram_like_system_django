from django.db import models
from accounts.models import Account

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(Account, on_delete=models.CASCADE)
    string = models.CharField(default='like',max_length=20)

    def __str__(self):
        return self.title

    def pub_date_fix(self):
       return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class voted_product(models.Model):
    vote_number = models.CharField(max_length=100,default="voted")
    product_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    string = models.CharField(default='like', max_length=20)

    # def __str__(self):
    #     return self.vote_number
