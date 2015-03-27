from django.db import models

# Create your models here.
from sections.models import CourseSection


class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True)
    section = models.ForeignKey(CourseSection)
    #variations = models.ManyToManyField(Variation, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=30.00, max_digits=1000, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.section.title


