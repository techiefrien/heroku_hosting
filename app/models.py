from django.db import models

# Create your models here.

class catagory(models.Model):
    catagory_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.catagory_name
    
    class Meta:
        ordering = ['catagory_name']



class products(models.Model):
    bname = models.CharField(max_length=100)
    catagory = models.ForeignKey(catagory , on_delete=models.CASCADE)
    bimg = models.ImageField(upload_to="book_cover")
    bfile = models.FileField(upload_to="pdf_files")
    author = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    download_count = models.CharField(max_length=100 , default=0)
    uploaded_at = models.DateField(auto_now_add=True)
    disc = models.TextField()

    
    def __str__(self) -> str:
        return self.bname
    
    class Meta:
        ordering = ['bname']
    