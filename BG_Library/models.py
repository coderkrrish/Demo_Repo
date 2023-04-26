from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length =100)
    qty = models.IntegerField()
    price = models.IntegerField()
    author = models.CharField(max_length=50)
    is_published = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "BG_Books"
        