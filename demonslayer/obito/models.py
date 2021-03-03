from django.db import models

# Create your models here.
class image(models.Model):
    Feedback=(
    ("e","excellent"),
    ("g","good"),
    ("b","bad"),
    )

    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)
    feedback=models.CharField(max_length=1,choices=Feedback)
    detail=models.TextField()
    def __str__(self):
        return (self.name)
class Video(models.Model):
    caption=models.CharField(max_length=10)
    video=models.FileField(upload_to="video/%y")
    thumb=models.FileField(upload_to="thumb/%y")
    def __str__(self):
        return (self.caption)
class Naruto(models.Model):
    caption=models.CharField(max_length=10)
    video=models.FileField(upload_to="video/%y")
    thumb=models.FileField(upload_to="thumb/%y")
    def __str__(self):
        return (self.caption)
class Demonslayer(models.Model):
    caption=models.CharField(max_length=10)
    video=models.FileField(upload_to="video/%y")
    thumb=models.FileField(upload_to="thumb/%y")
    def __str__(self):
        return (self.caption)
