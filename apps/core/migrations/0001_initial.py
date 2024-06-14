# Generated by Django 5.0.6 on 2024-06-14 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Registered at')),
                ('is_email_verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Recognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.ImageField(blank=True, upload_to='recognize/')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('html_file_name', models.CharField(blank=True, max_length=100, verbose_name='HTML file name')),
                ('doc_file', models.FileField(blank=True, upload_to='documents/')),
                ('child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.document')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.FloatField(default=0)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('total_spends', models.FloatField(blank=True, null=True)),
                ('prime_contributer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributer', to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=120, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('final_amount', models.FloatField(blank=True, null=True)),
                ('holders', models.ManyToManyField(blank=True, related_name='holder', to='core.customuser')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_item', to='core.expensebill')),
            ],
        ),
        migrations.CreateModel(
            name='UserSpentTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField(default=0)),
                ('seconds', models.IntegerField(default=0)),
                ('hours', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usertimespent', to='core.customuser')),
            ],
        ),
    ]