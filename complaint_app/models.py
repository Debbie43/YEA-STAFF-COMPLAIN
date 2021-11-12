from django.db import models

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(max_length=100)
    directorate = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    device = models.CharField(max_length=50)
    problem = models.CharField(max_length=150)
    short_description = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"<Name: {self.name}, Directorate: {self.directorate}, Problem: {self.problem}>"