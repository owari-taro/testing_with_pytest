from django.db import models

# Create your models here.

class Base(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Book(Base):
    id=models.UUIDField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=150)
    published_at=models.DateTimeField(null=True,help_text="発売日")
    version=models.IntegerField(default=1)
