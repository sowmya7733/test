from django.db import models

# Create your models here.
class Emp(models.Model):
    Ename = models.CharField(max_length=100)
    Eid = models.AutoField(primary_key=True)
    job = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


# class Dept2(models.Model):
#     Ename = models.CharField(max_length=100)
#     Dname = models.CharField(max_length=100)
#     Deptno = models.AutoField(primary_key=True)
#     Place = models.CharField(max_length=100)

    