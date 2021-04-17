from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=50)
    
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=1)
    category = models.CharField(default='other', max_length=50)
    unit = models.CharField(default='pcs', max_length=10)

    receipt = models.ForeignKey("receipt.Receipt", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Receipt(models.Model):

    owner = models.ForeignKey("account.Account", on_delete=models.CASCADE)

    purchase_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.owner.phone_number