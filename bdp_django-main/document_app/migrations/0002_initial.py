# Generated by Django 4.1.5 on 2023-01-04 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='onboardingdocument',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onboarding_document_user_id_model_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='miscdocument',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misc_document_user_id_model_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
