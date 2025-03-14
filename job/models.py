from django.db import models

'''
django models field :

-html widget 
-validation 
-db size
'''

JOB_TYPE=(('Full Time','Full Time'),
          ('Part Time','Part Time'),
          )


# Create your models here.
class job(models.Model): #table
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=12 , choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    def __str__(self):
    
          return self.title 

    
