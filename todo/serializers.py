from rest_framework import serializers
from .models import *

class todoitem(serializers.ModelSerializer):
    class Meta:
        model=todos
        fields=['id','titile','description','completed','created_at']