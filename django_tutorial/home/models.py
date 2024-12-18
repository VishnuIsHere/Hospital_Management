from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    def __str__(self):
        return self.dep_name
    
    
class Doctors(models.Model):
    doc_name = models.CharField( max_length=200)
    doc_spec = models.CharField( max_length=200)
    dep_name = models.ForeignKey("Departments",on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', height_field=None, width_field=None, max_length=None)    
    def __str__(self):
        return 'Dr. ' + self.doc_name + '-('+ self.doc_spec +')'
    
    
class Booking(models.Model):
    p_name = models.CharField( max_length=200)
    p_phone = models.CharField( max_length=100)
    p_email = models.EmailField(null=True, blank=True)  # Adjust as per your requirements
    doc_name = models.ForeignKey("Doctors",on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)