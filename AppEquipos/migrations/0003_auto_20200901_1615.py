# Generated by Django 3.0.8 on 2020-09-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEquipos', '0002_auto_20200901_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='HDD',
            field=models.CharField(choices=[('NO', 'NO'), ('especifica', 'SE ESPECIFICA EN NOTAS'), ('2.5m', 'Mecanico 2.5'), ('3.5m', 'Mecanico 3.5')], default='type_hdd', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='SSD',
            field=models.CharField(choices=[('NO', 'NO'), ('especifica', 'SE ESPECIFICA EN NOTAS'), ('m.2 sata', 'M.2 SATA'), ('m.2 pcie', 'M.2 PCIE'), ('2.5" sata', '2.5" SATA')], default='type_ssd', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='frecuencia',
            field=models.CharField(choices=[('2133 mHz', '2133 MHz'), ('1200 mHz', '1200 MHz'), ('NO', 'NO'), ('1600 mHz', '1600 MHz'), ('2666 mHz', '2666 MHz'), ('2000 mHz', '2000 MHz'), ('1866 mHz', '1866 MHz'), ('1333 mHz', '1333 MHz'), ('1066 mHz', '1066 MHz'), ('2400 mHz', '2400 MHz')], default='frecuencia', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='ranuras',
            field=models.CharField(choices=[('3', '3'), ('rows of chips', 'Rows of chips'), ('1', '1'), ('2', '2'), ('4', '5')], default='ranuras', max_length=15),
        ),
    ]
