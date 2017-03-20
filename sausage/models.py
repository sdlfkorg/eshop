from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name = "標籤名稱", max_length = 100)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "標籤"
        verbose_name_plural = "標籤"
        
class Category(models.Model):
    name = models.CharField(verbose_name = "分類名稱", max_length = 100)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "分類"
        verbose_name_plural = "分類"

class Sausage(models.Model):
    name = models.CharField(verbose_name="商品名稱", max_length=255)
    desription = models.TextField(
    verbose_name="商品敘述", 
    default="", 
    blank=True
    )
    #verbose_name="商家", max_length=255, default="", blank=True 
    created = models.DateTimeField(verbose_name="新增時間", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="更新時間", auto_now=True)
    published = models.DateTimeField(verbose_name="上架時間", null=True)
    
    image = models.FileField(null=True, blank=True)


    original_price = models.PositiveIntegerField(verbose_name="原價", default=0)
    current_price = models.PositiveIntegerField(verbose_name="售價", default=0)
    
    tag = models.ForeignKey(
    Tag, 
    verbose_name="標籤", 
    null=True, 
    blank=True
    )    
    
    category = models.ForeignKey(
    Category,
    verbose_name = "商品分類",
    null=True,
    blank=True
    )
    
    place_of_origin = models.TextField(verbose_name="產地", default="", blank=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "香腸"
        verbose_name_plural = "香腸"
        ordering = ['-created']
        
        
        