from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

class TODOModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False, default=None)
    Title = models.CharField(max_length = 100)
    Description = models.TextField(default=None)
    Important = models.BooleanField(default=None)
    DateTime = models.DateTimeField(default=timezone.now)

    def update(self, instance, validated_data):
        instance.Title = validated_data.get('Title', instance.Title)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.Important = validated_data.get('Important', instance.Important)
        instance.DateTime = validated_data.get('DateTime', instance.DateTime)
        instance.save()
        return instance