# -*- coding: utf-8 -*-
from django.db import models

class Series(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Underwear(models.Model):
    idu = models.CharField(max_length=30)
    series = models.ForeignKey(Series)
    availableM = models.IntegerField()
    availableL = models.IntegerField()
    availableXL = models.IntegerField()
    color = models.ForeignKey(Color, blank=True, null=True)
    def __unicode__(self):
        return self.idu
    class Meta:
        ordering = ['-availableM', 'series']

class Purchase(models.Model):
    purchase_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    totalprice = models.DecimalField(max_digits=9, decimal_places=2)
    phone_number = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    post_office = models.CharField(max_length=4)
    divisions = models.CharField(max_length=1, choices=(("a", "Доставка наложенным платежом"),("b", "100% предоплата на карту Приват Банка*"),))
    underwear = models.CharField(max_length=200)
    comment = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.first_name