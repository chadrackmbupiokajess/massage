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

class HomePageContent(models.Model):
    intro_title = models.CharField(max_length=200, default="Une approche dédiée à votre bien-être")
    intro_text = models.TextField(default="Chaque séance est une invitation au lâcher-prise...")
    cta_title = models.CharField(max_length=200, default="Prêt(e) à vous accorder une pause ?")
    cta_text = models.TextField(default="N'attendez plus pour prendre soin de vous...")

    def __str__(self):
        return "Contenu de la page d'accueil"

    # Singleton pattern: ensure only one instance exists
    def save(self, *args, **kwargs):
        self.pk = 1
        super(HomePageContent, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True, help_text="Afficher ce témoignage sur la page d'accueil")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'"{self.quote[:30]}..." - {self.author}'
