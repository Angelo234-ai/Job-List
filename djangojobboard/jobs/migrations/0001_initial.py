# Generated by Django 3.2.9 on 2022-06-22 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=50)),
                ('company_website', models.URLField()),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.CharField(max_length=50)),
                ('remote', models.BooleanField(default=False)),
                ('salary', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SponsoredJobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_until', models.DateTimeField()),
                ('stripe_payment_intent_id', models.CharField(max_length=150)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsored_posts', to='jobs.job')),
            ],
        ),
    ]
