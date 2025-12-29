from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class CarouselSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='carousel/')
    order = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage de la diapositive")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
