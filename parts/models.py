from django.db import models


class Parts(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
