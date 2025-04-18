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
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'title', 'course_code', 'description', 'duration', 'teacher']
        
    def validate_course_code(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Course code must be at least 5 characters long.")
        return value
    
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        return value
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
    
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value
    
    def validate_teacher(self, value):
        if not models.Teacher.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Teacher does not exist.")
        return value
    
    def validate(self, data):
        if models.Course.objects.filter(course_code=data['course_code']).exists():
            raise serializers.ValidationError("Course code already exists.")
        return data
    
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description', 'course', 'teacher']
        
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
    
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value
    
    def validate_course(self, value):
        if not models.Course.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Course does not exist.")
        return value
    
    def validate_teacher(self, value):
        if not models.Teacher.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Teacher does not exist.")
        return value

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email', 'password', 'phone_number', 'address', 'qualification', 'interested_catedories']
        
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value
    
    def validate_phone_number(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits long.")
        return value
    
    def validate_interested_catedories(self, value):
        if not models.CourseCategory.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Course category does not exist.")
        return value
