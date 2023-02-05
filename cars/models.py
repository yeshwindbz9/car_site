from django.db import models

# Create your models here.
class Car(models.Model):
    # pk is created automatically as id
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.brand} {self.model} was released in {self.year} (id: {self.id})"
