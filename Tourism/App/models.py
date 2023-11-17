from django.db import models

# Create your models here.
class package(models.Model):
    place=models.CharField(max_length=50)
    duriation=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    images=models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.place

class testimonials(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=850)
    images=models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name


class contact_detail(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):
        return self.name
    
class events(models.Model):
    images=models.ImageField(upload_to='uploads/')
    message=models.CharField(max_length=500)
    description=models.CharField(max_length=2000)

    
class sub_packages(models.Model):
     destination=models.CharField(max_length=50)
     day=models.CharField(max_length=20)
     night=models.CharField(max_length=20)
     price=models.CharField(max_length=20)
     description=models.CharField(max_length=2000)
     destination1=models.CharField(max_length=20)
     destination2=models.CharField(max_length=20)
     destination3=models.CharField(max_length=20)
     destination_des1=models.CharField(max_length=1000)
     destination_des2=models.CharField(max_length=1000)
     destination_des3=models.CharField(max_length=1000)
     image=models.ImageField(upload_to='uploads/')
     image1=models.ImageField(upload_to='uploads/')
     image2=models.ImageField(upload_to='uploads/')
     image3=models.ImageField(upload_to='uploads/')
     pack=models.ForeignKey(package, on_delete=models.CASCADE)
     def __str__(self):
        return self.destination
     
    
