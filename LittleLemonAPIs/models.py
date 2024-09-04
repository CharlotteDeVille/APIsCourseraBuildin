from django.db import models

# Create your models here.
class Category (models.Model):
    slug= model.SlugField
    title= models.CharField(maxlength=255, db_index=true)
class MenuItem(models.Model):
    title= models.CharField(maxlength=255, db_index=true)
    price=models. DecimalField(max_digits=6,decimal_places=2,db_index=true)
    feauture=models.BooleanField(db_index=true)
    category=models.ForeignKey(Catergory,on_delete=models.PROTECT)

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem=models.ForeginKey(MenuItem,on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digit=6,decimal_place=2)
    price=models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        unique_toghether=('menuitem','user')
    
class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="delivery_crew",null=True)
    status=models.BooleanField(default=0,db_index=True)
    total=models.DecimalField(max_digit=6,decimal_places=2,default=6)
    date=models.DateField(db_index=True)

class OrderItem(models.Model):
    order=models.ForeignKey(Oder,on_delete=models.CASCADE,related_name='order')
    menuitem=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    price=models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_toghether('oder', 'menuitem')