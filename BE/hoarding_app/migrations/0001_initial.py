# Generated by Django 3.1.7 on 2021-07-07 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=64)),
                ('list_type', models.CharField(choices=[('For sale', 'For sale'), ('For exchange', 'For exchange'), ('For free', 'For free')], max_length=12)),
                ('is_anonymous', models.CharField(choices=[('Keep me anonymous', 'Keep me anonymous'), ('Use name', 'Use name')], max_length=18)),
                ('is_favourite', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Furniture', 'Furniture'), ('Machinery', 'Machinery'), ('Office equipment', 'Office equipment'), ('Home equipment', 'Home equipment'), ('Gym equipment', 'Gym equipment'), ('Games', 'Games'), ('Electronics', 'Electronics'), ('Wood materials', 'Wood materials'), ('Toiletry', 'Toiletry'), ('Plastic', 'Plastic'), ('Art frames', 'Art frames'), ('Cloth', 'Cloth'), ('Jewelry', 'Jewelry')], max_length=20)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_image', models.ImageField(max_length=120, upload_to='images/%Y/%m/%d/')),
                ('iteme', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hoarding_app.item')),
            ],
        ),
        migrations.CreateModel(
            name='Free_exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ever_given', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('moment_given', models.TextField()),
                ('love_most', models.CharField(max_length=64)),
                ('why_this', models.TextField()),
                ('change_world', models.TextField()),
                ('item_no', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='free_exercise', to='hoarding_app.item')),
            ],
        ),
    ]