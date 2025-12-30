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
    testimonials_title = models.CharField(max_length=200, default="Ce que mes client(e)s en disent")
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

class AboutPageContent(models.Model):
    title = models.CharField(max_length=200, default="Mon approche du bien-être")
    main_text = models.TextField(default="Passionnée par les thérapies manuelles...")
    philosophy_text = models.TextField(default="Ma philosophie repose sur une écoute attentive...")
    commitments_title = models.CharField(max_length=200, default="Mes engagements pour votre sérénité")
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Image pour la page À Propos")

    def __str__(self):
        return "Contenu de la page À Propos"

    # Singleton pattern
    def save(self, *args, **kwargs):
        self.pk = 1
        super(AboutPageContent, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Commitment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactPageContent(models.Model):
    title = models.CharField(max_length=200, default="Prenons contact")
    subtitle = models.TextField(default="Pour toute question ou pour prendre rendez-vous...")
    email_title = models.CharField(max_length=100, default="Email")
    email = models.EmailField(default="contact@bienetre.com")
    phone_title = models.CharField(max_length=100, default="Téléphone")
    phone = models.CharField(max_length=50, default="06 12 34 56 78")
    address_title = models.CharField(max_length=100, default="Adresse")
    address = models.CharField(max_length=200, default="Paris, France")

    def __str__(self):
        return "Contenu de la page de Contact"

    # Singleton pattern
    def save(self, *args, **kwargs):
        self.pk = 1
        super(ContactPageContent, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
