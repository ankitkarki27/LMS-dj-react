from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        # fields = '__all__'
        fields = ['id', 'full_name', 'email', 'password', 'phone_number', 'qualification', 'address']
        
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value
    
