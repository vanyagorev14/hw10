from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name', max_length=150, verbose_name='first name')),
                ('family_name', models.CharField( help_text='Enter last name', max_length=150, verbose_name='family name')),
                ('email', models.EmailField(help_text='Enter email', max_length=254, verbose_name='email address')),
            ],
        ),
    ]