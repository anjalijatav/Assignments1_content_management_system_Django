from django.contrib.auth import get_user_model

from rest_framework import serializers

from authour.userfield  import Userfield,UserfieldManager
from authour.contentfield import  ContentfieldManager,Contentfield
class ContentfieldSerializer(serializers.ModelSerializer):
    """Serialzier from content field object"""

    class Meta:
        model = Contentfield
        fields =(
            'title',
            'body',
            'summary',
            'document',
            'categories',
        )
        read_only_fields = ('title',)

    def create(self, validated_data):
        print(validated_data)
        user_id = get_user_model()
        return Contentfield.objects.create_content_data(user_id=user_id, **validated_data)

class UserfieldSerializer(serializers.ModelSerializer):
    """Serializer for users object"""
    class Meta:
        # model = get_user_model()
        model = Userfield
        fields = (
            'email',
            'name',
            'phone',
            'address',
            'city',
            'country','pincode','state',
        )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return Userfield.objects.create_user(**validated_data)
