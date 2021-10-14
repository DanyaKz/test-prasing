from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Resource(models.Model):
    resource_name = models.CharField(max_length = 255, null = True , blank = True)
    resource_url = models.CharField(max_length = 255, null = True , blank = True)
    top_tag = models.CharField(max_length = 255)
    bottom_tag = models.CharField(max_length = 255)
    title_cut = models.CharField(max_length = 255)
    date_cut = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.resource_name}'
    


class Item(models.Model):
    res_id = models.ForeignKey(Resource , on_delete = models.DO_NOTHING)
    link = models.CharField(max_length = 255)
    title = models.TextField()
    content = models.TextField()
    nd_date = models.IntegerField(validators=[MaxValueValidator(11)])
    s_date = models.IntegerField(validators=[MaxValueValidator(11)])
    not_date = models.DateField()

    def __str__(self):
        return f'{self.link} - {self.title} - {self.not_date}'