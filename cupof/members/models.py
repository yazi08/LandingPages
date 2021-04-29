from django.db import models

class Members (models.Model):
    name = models.TextField(max_length = 20)
    chai_or_coffee = models.TextField(max_length = 20)

    def __str__(self):
        return f"{self.name,self.chai_or_coffee}"
