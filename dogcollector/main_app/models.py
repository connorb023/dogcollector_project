# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# new code above

from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# Create your models here.

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
      return f'{self.color} {self.name}'

  def get_absolute_url(self):
      return reverse('toys_detail', kwargs={'pk': self.id})

class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
   # Add the M:M relationship
  toys = models.ManyToManyField(Toy)
  # Add the foreign key linking to a user instance
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'dog_id': self.id})


# Add new Feeding model below dog model

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  
  # Create a dog_id FK
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

# change the default sort
  class Meta:
    ordering = ['-date']
    