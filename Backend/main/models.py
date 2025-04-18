from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    qualification=models.CharField(max_length=200)
    address=models.TextField(("Address"), max_length=255, blank=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        # verbose_name = "Course Category"
        verbose_name_plural = "1. Teachers"
        
# Course Model
class Course(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    duration = models.IntegerField()   
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        # verbose_name = "Course Category"
        verbose_name_plural = "2. Courses"
    
# course-category model
class CourseCategory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        # verbose_name = "Course Category"
        verbose_name_plural = "3. Course Categories"
    
# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    address=models.TextField(("Address"), max_length=255, blank=True)
    qualification=models.CharField(max_length=200)
    interested_catedories=models.ManyToManyField(CourseCategory, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        # verbose_name = "Course Category"
        verbose_name_plural = "4. Students"
    