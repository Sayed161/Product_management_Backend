from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()



class productsModel(models.Model):
    Product_name = models.CharField(max_length=200)
    categories =(
        ('Accessories', 'Accessories'),
        ('Computers', 'Computers'),
        ('Electronics', 'Electronics'),
        ('Furniture', 'Furniture'),
        ('Garden', 'Garden'),
        ('Home', 'Home'),
        ('Kitchen', 'Kitchen'),
        ('Fruits', 'Fruits'),
        ('shoes', 'Shoes'),
        ('Sports', 'Sports'),
        ('Toys', 'Toys'),
        ('Travel', 'Travel'),
        ('Watches', 'Watches'),
        ('Others', 'Others'),
    )
    Category = models.CharField(max_length=40,choices=categories)
    SubCategory = models.CharField(max_length=40,choices=categories)
    Brand_choice = (
        ('Samsung','Samsung'),
        ('Apple','Apple'),
        ('Acer','Acer'),
        ('HP','HP'),
        ('Lenovo','Lenovo'),
        ('Asus','Asus'),
        ('Dell','Dell'),
        ('Toshiba','Toshiba'),
        ('Xiaomi','Xiaomi'),
        ('Other','Other'),
    )
    Brand = models.CharField(max_length=40,choices=Brand_choice)
    Unit_choice = (
        ('pc','pc'),
        ('kg','kg'),
        ('box','box'),
        ('liter','liter'),
        ('m','m'),
        ('cm','cm'),
    )
    Unit = models.CharField(max_length=40,choices=Unit_choice)
    SKU = models.CharField(max_length=300)
    Minimum_Quantity = models.IntegerField()
    Quantity = models.IntegerField()
    Description = models.TextField()
    Tax_choice = (
        ('Sales Tax', 'Sales Tax'),
        ('Excise Tax', 'Excise Tax'),
    )
    Tax = models.CharField(max_length=30,choices=Tax_choice)
    Dicount_type = (
        ('percentage', 'Percentage'),
        ('Doller-Amount', 'Doller-Amount'),
        ('Buy-one-get-one', 'Buy-one-get-one'),
        ('volume-amount', 'Volume-Amount'),
        ('seasonal', 'Seasonal'),
        ('Early-Bird', 'EarlyBird'),
        ('Free-shipings', 'Free-Shipings'),
        ('Membership', 'Membership'),
        ('Referral', 'Referral'),
    )
    Discount =models.CharField(max_length=40,choices=Dicount_type)
    price = models.CharField(max_length=20)
    status_type =(
        ('Open', 'Open'),
        ('Close', 'Close'),
        ('Out of Stock', 'Out of Stock'),
        
        
    )
    Status= models.CharField(max_length=20,choices=status_type)
    product_image = models.ImageField(upload_to='product_image/')
    role_choices = (
        ('Seller', 'Seller'),
        ('Admin', 'Admin'),
    )
    Created_by = models.CharField(max_length=8, choices=role_choices,null=True)

    