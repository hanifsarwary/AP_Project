from rest_framework import serializers
from .models import Dialog, Message



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



class MessageSeenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['read']