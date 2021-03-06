# Generated by Django 4.0.4 on 2022-05-10 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('status', models.CharField(choices=[('pub', 'public'), ('sec', 'private')], max_length=20)),
                ('icon', models.ImageField(upload_to='chat/img/chats')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('icon', models.ImageField(upload_to='chat/img/users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Massages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massage', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eclipse.chats')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eclipse.users')),
            ],
        ),
        migrations.CreateModel(
            name='Chats_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.CharField(choices=[('A', 'Admin'), ('U', 'User')], max_length=20)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eclipse.chats')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eclipse.users')),
            ],
        ),
    ]
