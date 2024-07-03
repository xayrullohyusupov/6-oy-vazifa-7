from django.db import models

class Info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=10)
    message=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name},{self.email},{self.subject},{self.message}"

class Best(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='best_images/')

    def __str__(self):
       return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='meetings/')
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
     return self.title