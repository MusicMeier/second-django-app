from django.db import models

# Create your models here.
class Bear(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()

  def __str__ (self):
    return "name: " + self.name + ", age:" + str(self.age)

class PicnicBasket(models.Model):
  sandwiches = models.BooleanField()
  bear = models.ForeignKey(Bear, related_name='picnicbaskets', on_delete=models.CASCADE)

  def __str__(self):
    return "{ sandwiches: %s}" %{self.sandwiches}