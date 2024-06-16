from rest_framework import serializers

from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    # special_client = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = [
            'name',
            'customer',
            'date_added',
            'special_client'
        ]

    # def special_client(self, obj):
    #     special_client = obj.special_client()
    #     if special_client is not None:
    #         return special_client
    #     return 'ordinary'



class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'customer',
            'date_added',
        ]
