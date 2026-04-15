from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Programme(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='programme_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.programme.title}"