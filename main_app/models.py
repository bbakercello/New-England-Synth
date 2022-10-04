from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=150, default="BLANK")
    img = models.CharField(max_length=250, default="BLANK")

    def __Str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Module(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    info = models.TextField(max_length=500)
    function = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="manufacturer", default="BLANK")
    created_at = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.name

    class Meta:
        ordering = ['name']



