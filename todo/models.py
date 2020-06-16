from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # add the function below to override the class inheritence whereby the item names have understandable names in the admin
    # (comment this out to see what I mean)
    def __str__(self):
        return self.name
