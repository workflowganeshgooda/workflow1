from django.db import models

class CustomManager(models.Manager):
    def sortbylth(request):
        return super().filter(active='y').order_by('book_price')