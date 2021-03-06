# Generated by Django 3.0.6 on 2020-06-13 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('pair', models.CharField(max_length=15, verbose_name='交易对')),
                ('enable', models.BooleanField(default=True, verbose_name='启用')),
                ('start_time', models.DateTimeField(null=True, verbose_name='启动时间')),
                ('ping_time', models.DateTimeField(null=True, verbose_name='心跳时间')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='创建于')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='修改于')),
                ('credential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robots', to='credentials.Credential', verbose_name='交易所凭据')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='robots', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '机器人',
                'verbose_name_plural': '机器人',
            },
        ),
    ]
