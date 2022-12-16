from django.db import models

class Department(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=45)
    address = models.CharField(db_column='address', max_length=45)
    manager = models.CharField(db_column='manager', max_length=45)
    tel = models.CharField(db_column='tel',max_length=45)  
    school_id = models.ForeignKey('School', db_column='school_id', on_delete=models.CASCADE)
    class Meta:
        db_table = 'department'
        managed=False

class Site(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=45)
    usage = models.CharField(db_column='usage', max_length=45)
    price = models.IntegerField(db_column='price', max_length=45)
    rule = models.DateField(db_column='rule',max_length=45)
    picture = models.CharField(db_column='picture', max_length=45)
     
    
    department_id = models.ForeignKey('Department', db_column='department_id', on_delete=models.CASCADE)
    class Meta:
        db_table = 'site'
        managed=False

class Duration(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    date= models.DateField(db_column='date')
    start = models.CharField(db_column='start', max_length=45)
    end = models.CharField(db_column='end', max_length=45)
    rent_status = models.IntegerField(db_column='rent_status', max_length=45)
    site_id= models.ForeignKey('Site', db_column='site_id', on_delete=models.CASCADE)
    class Meta:
        db_table = 'duration'
        managed=False