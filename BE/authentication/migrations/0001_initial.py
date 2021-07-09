# Generated by Django 3.1.7 on 2021-07-08 02:49

import authentication.models
import authentication.passwordValidators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('password2', authentication.passwordValidators.PasswordModelField(max_length=100, verbose_name='confirm password')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='e.g Nigeria +234...', max_length=128, region=None, unique=True, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=1000, verbose_name='address')),
                ('state', models.CharField(max_length=150, verbose_name='state')),
                ('ID_number', models.CharField(max_length=150, verbose_name='ID number')),
                ('national', models.ImageField(blank=True, null=True, upload_to='Identity/national', verbose_name='national ID card')),
                ('school', models.ImageField(blank=True, null=True, upload_to='Identity/school', verbose_name='school ID card')),
                ('local_gov', models.CharField(max_length=150, verbose_name='local government area')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_verified', models.BooleanField(default=False, help_text='Designates whether this users email is verified.', verbose_name='email verified')),
                ('is_verified', models.BooleanField(default=False, help_text='Designates whether this users identity is verified.', verbose_name='users identity verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', authentication.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('address', models.CharField(max_length=1000, verbose_name='address')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('ID_number', models.CharField(max_length=150, verbose_name='ID number')),
                ('national', models.ImageField(blank=True, null=True, upload_to='Identity/national', verbose_name='national ID card')),
                ('school', models.ImageField(blank=True, null=True, upload_to='Identity/school', verbose_name='school ID card')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
