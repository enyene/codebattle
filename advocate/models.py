from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/logo')
    summary = models.CharField(max_length=200)
    href = models.URLField()
    

    def __str__(self):
        return self.name


 

    class Meta:
        verbose_name_plural = 'Company'

class Links(models.Model):
    youtube = models.URLField()
    twitter = models.URLField()
    github = models.URLField()

    class Meta:
        verbose_name_plural = 'Links'

class Advocate(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='advocate/pics')
    short_bio = models.CharField(max_length=200)
    long_bio = models.TextField()
    advocate_years_experience = models.IntegerField()
    company = models.ForeignKey('Company',on_delete=models.CASCADE,null=True)
    links = models.ForeignKey('Links',on_delete=models.CASCADE,null=True)

   




class Companies(models.Model):
    company = models.ForeignKey('Company',on_delete=models.CASCADE)
    advocates = models.ManyToManyField('Advocate')




    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company.name