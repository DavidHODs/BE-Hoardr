from rest_framework import serializers
from .models import Item, Image, Free_exercise

class ImageNestedWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'item_image']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageNestedWriteSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'images', 'list_type', 'is_anonymous', 
                  'is_favourite', 'price']# 'uploaded_date', 'is_active',, 'description', 'location', 'category'

    def create(self, validated_data):
        images = validated_data['images']
        del validated_data['images']

        item = Item.objects.create(**validated_data)
        for image in images:
            obj = Image.objects.create(**image)
            item.images.add(obj)

        item.save()

        return item

class ItemIDSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageNestedWriteSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'images', 'location', 'list_type', 'is_anonymous', 
                  'is_favourite', 'price']# 'uploaded_date', 'is_active',, 'category'

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'item_image', 'iteme']

class FreeExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Free_exercise
        fields = ['id', 'ever_given', 'moment_given', 'love_most', 'why_this', 'change_world', 'item_no']