from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Ticket(models.Model):
    # Got help from Sohail Aslam in study hall here.
    TICKET_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),
    ]
    title = models.CharField(max_length=80)
    time_and_date_filed = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ticket_status = models.CharField(max_length=24, 
                                     choices=TICKET_CHOICES,
                                     default='New')
    user_filed_ticket = models.ForeignKey(CustomUserModel, 
                                          on_delete=models.CASCADE, 
                                          related_name='user_filed')
    user_assigned_ticket = models.ForeignKey(CustomUserModel, 
                                             on_delete=models.CASCADE, 
                                             null=True,
                                             related_name='user_assigned')
    user_completed_ticket = models.ForeignKey(CustomUserModel, 
                                              on_delete=models.CASCADE,
                                              null=True,
                                              related_name='user_completed')

    def __str__(self):
        return self.title