from django.db import models
from django.contrib.auth.models import User

class StudentRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField()
    backlogs = models.IntegerField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    fees_paid_receipt = models.FileField(upload_to='receipts/', null=True, blank=True)

    def __str__(self):
         return self.name
