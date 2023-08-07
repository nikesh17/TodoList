from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    # to not create a physical table
    class Meta:
        abstract = True 
        
    
class Category(TimeStampModel):
    name =  models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural ="Categories"
        
    def __str__(self):
        return self.name
    
class Label(TimeStampModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Priority(models.TextChoices):
    LOWEST = "lowest", "Lowest"
    LOW = "low", "Low"
    MEDIUM = "medium","Medium"
    HIGH = "high", "High"
    HIGHEST = "highest","Highest"
   
class Task(TimeStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) #blank for html, null for database
    image = models.ImageField(upload_to="todolist", blank=True, null=True)
    task_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=100, choices = Priority.choices, default = Priority.LOWEST)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    labels =  models.ManyToManyField(Label, blank = True)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name