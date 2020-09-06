from django.db import models

# Create your models here.


class PostMarcas(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Post(models.Model):

    STATUS_CHOICES1={
         ('1','1'),
         ('2','2'),#ranuras
         ('3','3'),
         ('4','5'),
         ('rows of chips','Rows of chips')
    }

    STATUS_CHOICES2={
         ('2.5m','Mecanico 2.5'),
         ('3.5m','Mecanico 3.5'), #HDD
         ('especifica','SE ESPECIFICA EN NOTAS'),
         ('NO','NO')
    }
    STATUS_CHOICES3={
         ('1066 mHz','1066 MHz'),
         ('1200 mHz','1200 MHz'),
         ('1333 mHz','1333 MHz'),     #frecuencias mhz
         ('1600 mHz','1600 MHz'),
         ('1866 mHz','1866 MHz'),
         ('2000 mHz','2000 MHz'),
         ('2133 mHz','2133 MHz'),
         ('2400 mHz','2400 MHz'),
         ('2666 mHz','2666 MHz'),
         ('NO','NO')
    }
    STATUS_CHOICES4={
         ('m.2 sata','M.2 SATA'),
         ('2.5" sata','2.5" SATA'),
         ('m.2 pcie','M.2 PCIE'), #SSD
         ('especifica','SE ESPECIFICA EN NOTAS'),
         ('NO','NO')
    }

    marca= models.ForeignKey(PostMarcas,default=None,on_delete=models.CASCADE)
    modelo= models.CharField(max_length=45)
    ranuras=models.CharField(max_length=15,choices=STATUS_CHOICES1,default="ranuras")
    frecuencia=models.CharField(max_length=15,choices=STATUS_CHOICES3,default="frecuencia")
    SSD=models.CharField(max_length=20,choices=STATUS_CHOICES4,default="type_ssd")
    HDD=models.CharField(max_length=20,choices=STATUS_CHOICES2,default="type_hdd")
    notas=models.TextField()
    imagePortada= models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.modelo

class Images(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return str(self.post.marca)
