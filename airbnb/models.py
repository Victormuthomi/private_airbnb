from django.db import models


# Create your models here.

class Airbnb(models.Model):
    """Define the fields for the airbnb"""
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    rooms = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    avalability = models.BooleanField(default=True)
    services = models.TextField()
    

    def __str__(self):
          """Print the name of the airbnb """
          return self.name

class Airbnbimage(models.Model):
     """Define the fields for the images"""
     airbnb = models.ForeignKey(Airbnb, related_name='images', on_delete= models.CASCADE)
     image = models.ImageField(upload_to='images/', default='default.jpeg')

     def __str__(self):
          """Print the name of the airbnb image is being uplooded for"""
          return str(self.airbnb) + ' ' + 'images'

class Customer(models.Model):
     """Define the fields for the customers"""
     name = models.CharField(max_length=20)
     email = models.EmailField()
     phone_number = models.PositiveBigIntegerField()
     Id_number = models.PositiveBigIntegerField()
     booking_id= models.AutoField(primary_key=True)
     airbnb = models.ForeignKey(Airbnb, on_delete=models.CASCADE)
     Mpesa_code = models.CharField(max_length=20)
     date = models.DateTimeField(auto_now=True)

     def __str__(self):
          """Print the name of the customer"""
          return  'booking number ' + str(self.booking_id) + ' user ' + self.name + ' booking airbnb ' + str(self.airbnb) + ' on ' + self.date.strftime('%d %B %Y %H:%M')
     

class HomepageImages(models.Model):
    """Define the fields for homepage images"""
    PURPOSE_CHOICES = [
        ('airbnb', 'Airbnb Image'),
        ('mover', 'Mover Image'),
        # Add more choices here as needed
    ]

    image = models.ImageField(upload_to='images/', default='default.jpeg')
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='airbnb')

    def __str__(self):
        """Print the purpose of the image being uploaded"""
        return self.get_purpose_display()


     



