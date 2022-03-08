from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import student
#create the class

class studentserializers(serializers.HyperlinkedModelSerializer):  # basically it is given a hyperlink jiper click se data display krega
    class Meta:
        model = student
        fields = ('firstname','lastname')
