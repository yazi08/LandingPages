from django.db import models

class Coffee (models.Model):
    name = models.TextField()
    type_coffee = models.CharField(max_length=20)
    price = models.FloatField()
    img = models.ImageField(upload_to='coffee',null=True)

    def __str__(self):
        return f"{self.name, self.type_coffee,self.price}"