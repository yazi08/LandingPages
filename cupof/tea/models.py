from django.db import models

class Chai (models.Model):
    name = models.TextField()
    type_chai = models.CharField(max_length=20)
    price = models.FloatField()
    photo = models.ImageField('tea/гринфилд.jpg',upload_to='чай',null=True)

    def __str__(self):
        return f"{self.name, self.type_chai,self.price,self.photo}"

