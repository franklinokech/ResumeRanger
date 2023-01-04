from django.core.validators import FileExtensionValidator
from django.db import models


class JobSeeker(models.Model):
    cv = models.FileField(upload_to='cvs', validators=[FileExtensionValidator(['pdf'])])
    requirements = models.TextField(default='test default')
