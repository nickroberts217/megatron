# Generated by Django 2.1.3 on 2018-11-21 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('megatron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_id', models.CharField(db_index=True, max_length=10)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megatron.CustomerWorkspace')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='platformuser',
            unique_together={('platform_id', 'workspace')},
        ),
    ]