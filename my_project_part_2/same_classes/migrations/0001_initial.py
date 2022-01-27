# Generated by Django 4.0.1 on 2022-01-27 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlation_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_feedback', models.IntegerField(choices=[(1, 'yes'), (2, 'no')], null=True)),
                ('user_feedback_timestamp', models.DateTimeField(null=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]