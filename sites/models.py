from django.db import models

class Site(models.Model):
    def __unicode__(self):              
        return self.name
    name = models.CharField(max_length=200)
    
class Value(models.Model):
    site = models.ForeignKey(Site)
    a_value = models.DecimalField(max_digits=5, decimal_places=2)
    b_value = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField('date published')