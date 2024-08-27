from django.db import models

# Create your models here.


class books(models.Model):
    title=models.CharField(max_length=50)
    writer=models.CharField(max_length=30)
    image=models.ImageField()
    description =models.TextField()
    publish_date=models.DateField()
    isactive=models.BooleanField()
    
    def __str__(self):
        return f"{self.title}"
    
    # books(title="Kürk Mantolu Madonna",writer="Sabahattin Ali",image="KM_Madonna",description="güzel",publish_date=datetime.now,isactive=1)
    
    
class Category(models.Model):
    name=models.CharField(max_length=40)
    slug=models.CharField(max_length=50)
    