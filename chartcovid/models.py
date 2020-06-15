from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=50)
    total_cases = models.IntegerField(blank=True)
    new_cases = models.IntegerField(blank=True)
    total_deaths = models.IntegerField(blank=True)
    new_deaths = models.IntegerField(blank=True)
    total_recovered = models.IntegerField(blank=True)
    new_recovered = models.IntegerField(blank=True)
    active_cases = models.IntegerField(blank=True)
    serious_cases = models.IntegerField(blank=True)
    population = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.country
    