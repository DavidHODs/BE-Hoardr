from django.db import models

# Create your models here.
class Item(models.Model):
    FS = 'For sale'
    FE = 'For exchange'
    FF = 'For free'
    KA = 'Keep me anonymous'
    UN = 'Use name'
    Furniture = 'Furniture' 
    Machinery = 'Machinery' 
    Office_equipment = 'Office equipment'
    Home_equipment = 'Home equipment'
    Gym_equipment = 'Gym equipment'
    Games = 'Games'
    Electronics = 'Electronics' 
    Wood_materials = 'Wood materials'
    Toiletry = 'Toiletry'
    Plastic = 'Plastic'
    Art_frames = 'Art frames'
    Cloth = 'Cloth'
    Jewelry = 'Jewelry'

    LIST_CHOICES=[
        (FS, 'For sale'),
        (FE, 'For exchange'),
        (FF, 'For free')
    ]
    ANONYMOUS=[
        (KA, 'Keep me anonymous'),
        (UN, 'Use name')
    ]
    CATEGORIES=[
        (Furniture, 'Furniture'), 
        (Machinery, 'Machinery'), 
        (Office_equipment, 'Office equipment'), 
        (Home_equipment, 'Home equipment'), 
        (Gym_equipment, 'Gym equipment'), 
        (Games, 'Games'),
        (Electronics, 'Electronics'), 
        (Wood_materials, 'Wood materials'),
        (Toiletry, 'Toiletry'), 
        (Plastic, 'Plastic'), 
        (Art_frames, 'Art frames'), 
        (Cloth, 'Cloth'), 
        (Jewelry, 'Jewelry')
    ]

    title = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)
    list_type = models.CharField(choices=LIST_CHOICES, max_length=12)#, max_length=12
    is_anonymous = models.CharField(choices=ANONYMOUS, max_length=18)
    is_favourite = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORIES, max_length=20)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    item_image = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=120)
    iteme = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='images', default=1)

class Free_exercise(models.Model):
    Y = 'Yes'
    N = 'No'

    GIVEN = [
        (Y, 'Yes'),
        (N, 'No')
    ]

    ever_given = models.CharField(choices=GIVEN, max_length=3)
    moment_given = models.TextField()
    love_most = models.CharField(max_length=64)
    why_this = models.TextField()
    change_world = models.TextField()
    item_no = models.OneToOneField(Item, on_delete=models.SET_NULL, related_name='free_exercise', blank=True, null=True)#(collector, field, sub_objs, using)