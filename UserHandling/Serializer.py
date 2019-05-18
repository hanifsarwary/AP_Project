from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import hashers
from django.core.exceptions import ValidationError
import magic
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat


@deconstructible
class FileValidator(object):
    error_messages = {
     'max_size': ("Ensure this file size is not greater than %(max_size)s."
                  " Your file size is %(size)s."),
     'min_size': ("Ensure this file size is not less than %(min_size)s. "
                  "Your file size is %(size)s."),
     'content_type': "Files of type %(content_type)s are not supported.",
    }

    def __init__(self, max_size=None, min_size=None, content_types=()):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                'max_size': filesizeformat(self.max_size),
                'size': filesizeformat(data.size),
            }
            raise ValidationError(self.error_messages['max_size'],
                                   'max_size', params)

        if self.min_size is not None and data.size < self.min_size:
            params = {
                'min_size': filesizeformat(self.min_size),
                'size': filesizeformat(data.size)
            }
            raise ValidationError(self.error_messages['min_size'],
                                   'min_size', params)

        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = { 'content_type': content_type }
                raise ValidationError(self.error_messages['content_type'],
                                   'content_type', params)

    def __eq__(self, other):
        return (
            isinstance(other, FileValidator) and
            self.max_size == other.max_size and
            self.min_size == other.min_size and
            self.content_types == other.content_types
        )


class ProfileSerializer(ModelSerializer):
    validate_file = FileValidator(max_size=1024 * 1000,
                                  content_types=('application/json','image/jpeg'))
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    profile_pic = serializers.FileField(validators=[validate_file],allow_null=True)

    def create(self, validated_data):
         validated_data['password'] = hashers.make_password(validated_data['password'])
         return Profile.objects.create(**validated_data)

    class Meta:
        model = Profile
        fields = ('username','email', 'first_name','last_name','password','profile_pic')


class ProfileSendSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class GetFollowerFolloweeSerializer(ModelSerializer):

    class Meta:
        model = FollowerFollowing
        fields = '__all__'
        depth = 1


class FollowerFolloweeSerializer(ModelSerializer):

    class Meta:
        model = FollowerFollowing
        fields = '__all__'