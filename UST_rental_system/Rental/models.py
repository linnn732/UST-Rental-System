from django.db import models
from Member.models import School

class Department(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=45)
    address = models.CharField(db_column='address', max_length=45)
    manager = models.CharField(db_column='manager', max_length=45)
    tel = models.CharField(db_column='tel',max_length=45)  
    school_id = models.ForeignKey(School, db_column='school_id', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        managed=False

class Site(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=45)
    usage = models.CharField(db_column='usage', max_length=45)
    price = models.IntegerField(db_column='price')
    rule = models.DateField(db_column='rule',max_length=45)
    picture = models.CharField(db_column='picture', max_length=45)
     
    
    department_id = models.ForeignKey('Department', db_column='department_id', on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = 'site'
        managed=False

class Duration(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    date= models.DateField(db_column='date')
    start = models.IntegerField(db_column='start')
    end = models.IntegerField(db_column='end')
    rent_status = models.IntegerField(db_column='rent_status')
    site_id= models.ForeignKey('Site', db_column='site_id', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'duration'
        managed=False