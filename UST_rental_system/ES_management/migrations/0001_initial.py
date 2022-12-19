# Generated by Django 3.2.16 on 2022-12-18 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=45)),
                ('address', models.CharField(db_column='address', max_length=45)),
                ('manager', models.CharField(db_column='manager', max_length=45)),
                ('tel', models.CharField(db_column='tel', max_length=45)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('member_id', models.CharField(db_column='member_id', max_length=45)),
                ('name', models.CharField(db_column='name', max_length=45)),
                ('identity', models.CharField(db_column='identity', max_length=45)),
                ('sex', models.CharField(db_column='sex', max_length=45)),
                ('birthday', models.DateField(db_column='birthday')),
                ('tel', models.CharField(db_column='tel', max_length=45)),
                ('email', models.EmailField(db_column='email', max_length=45)),
                ('password', models.CharField(db_column='password', max_length=45)),
                ('image', models.ImageField(db_column='image', upload_to='member_img/')),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=45)),
                ('tel', models.CharField(db_column='tel', max_length=45)),
                ('address', models.CharField(db_column='address', max_length=45)),
                ('website', models.CharField(db_column='website', max_length=45)),
                ('image', models.ImageField(db_column='image', upload_to='school_img/')),
                ('public_private', models.CharField(db_column='public/private', max_length=45)),
                ('union', models.CharField(db_column='union', max_length=45)),
                ('school_system', models.CharField(db_column='school_system', max_length=45)),
            ],
            options={
                'db_table': 'school',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=45)),
                ('usage', models.CharField(db_column='usage', max_length=45)),
                ('amount', models.IntegerField(db_column='amount')),
                ('price', models.IntegerField(db_column='price')),
                ('picture', models.CharField(db_column='picture', max_length=45)),
                ('department_id', models.ForeignKey(db_column='department_id', on_delete=django.db.models.deletion.CASCADE, to='ES_management.department')),
            ],
            options={
                'db_table': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='Rent_Equipment',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('date', models.CharField(db_column='date', max_length=45)),
                ('amount', models.IntegerField(db_column='amount')),
                ('return_address', models.IntegerField(db_column='return_address')),
                ('state', models.IntegerField(db_column='state')),
                ('timestamp', models.DateTimeField(db_column='timestamp', max_length=45)),
                ('equipment_id', models.ForeignKey(db_column='equipment_id', on_delete=django.db.models.deletion.CASCADE, to='ES_management.equipment')),
                ('member_id', models.ForeignKey(db_column='member_id', on_delete=django.db.models.deletion.CASCADE, to='ES_management.member')),
            ],
            options={
                'db_table': 'rent_equipment',
            },
        ),
    ]
