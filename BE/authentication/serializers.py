from rest_framework import serializers
from authentication.models import User, Profile

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=10, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'country', 'state', 'local_gov', 'password', 'password2', 'token')

        read_only_fields = ['token']


    def validate(self, attrs):
	    if attrs['password'] != attrs['password2']:
	        raise serializers.ValidationError({"password": "Password fields didn't match."})

	    return attrs


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class EmailVerificationSerializer(serializers.ModelSerializer):

	token = serializers.CharField(max_length=1000)

	class Meta:
		model = User
		fields = ('token')



class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

        read_only_fields = ['token']



class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'email', 'ID_number', 'national', 'school', 'token')

        read_only_fields = ['token']


    def put(self, instance, validated_data):

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.address = validated_data['address']
        instance.phone_number = validated_data['phone_number']
        instance.email = validated_data['email']
        instance.ID_number = validated_data['ID_number']
        instance.national = validated_data['national']
        instance.school = validated_data['school']

        instance.save()

        return instance


# change password


class ChangePasswordSerializer(serializers.Serializer):

    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


  
