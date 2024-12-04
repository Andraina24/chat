from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Chat with{self.user.username}: {self.message}'


class FundedFirm(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_email = models.EmailField(unique=True)
    amount_funded = models.DecimalField(max_digits=12, decimal_places=2)
    date_funded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name