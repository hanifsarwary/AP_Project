from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
import magic
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat



class GETDialogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dialog
        fields = '__all__'
        depth = 1


class DialogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dialog
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        dialog = validated_data['dialog']
        owner = dialog.owner
        opponent = dialog.opponent
        return message


class GETMessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = '__all__'
        depth = 1

class MessageSeenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['read']


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


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

# we must always make different GET and POST serializer so we can easily manipulate our desired fields and we can also gain more control
#depth should only be used in the POST serializer where we are not concerned abaout adding data into database

class PostPictureSerializer(ModelSerializer):
    validate_file = FileValidator(max_size=1024 * 1000, content_types=('application/json', 'image/jpeg','image/png'))
    picture = serializers.FileField(validators=[validate_file], allow_null=True)
    # post = PostSerializer()

    class Meta:
        model = PostPicture
        fields = ['picture','post']
        # depth = 2


class PostLikeSerializer(ModelSerializer):

    class Meta:
        model = PostLike
        fields = '__all__'


class PostCommentSerializer(ModelSerializer):

    class Meta:
        model = PostComment
        fields = '__all__'


class GroupSerializer(ModelSerializer):

    class Meta:

        model = Group
        fields = '__all__'


class GroupMemberSerializer(ModelSerializer):

    class Meta:

        model = GroupMembers
        fields = '__all__'


class GroupPostSerializer(ModelSerializer):

    class Meta:

        model = GroupPost
        fields = '__all__'