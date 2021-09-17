from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancytranslation',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='vacancytranslation',
            name='salary',
            field=models.CharField(max_length=250, verbose_name='salary'),
        ),
        migrations.AlterField(
            model_name='vacancytranslation',
            name='title',
            field=models.CharField(max_length=250, verbose_name='title'),
        ),
    ]
