from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Issue(models.Model):
    PRIORITY_CHOICES = (
        ('Lowest', 'Lowest'),
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Highest', 'Highest'),
    )
    TASK_CHOICES = (
        ('OP', 'Open'),
        ('IN', 'In Progress'),
        ('CL', 'Closed')
    )
    user = models.ForeignKey(
        User,
        related_name='issues',
        on_delete=models.CASCADE
    )

    title = models.CharField(
        _('Title'),
        max_length=200
    )
    description = models.TextField(
        _('Description'),
    )
    end_date = models.DateTimeField(
        _('End Date'),
        blank=True,
        null=True
    )
    priority = models.CharField(
        _('Priority'),
        choices=PRIORITY_CHOICES,
        max_length=10,
        default='Lowest'
    )
    status = models.CharField(
        _('Status'),
        choices=TASK_CHOICES,
        max_length=2,
        default='OP'
    )

    def __str__(self):
        return f"#{self.pk} {self.title}"
