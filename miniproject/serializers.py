from rest_framework import serializers
from .models import Career

class CareerSerializer(serializers.HyperlinkedModelSerializer):
    # careers = serializers.HyperlinkedRelatedField(
    #     view_name='career_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta: 
        model = Career
        fields = ('id','role','industry','comnpany')