from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Results_course'
        
    def __str__(self):
        return self.course_code + " " + self.course_number + " " + self.course_name

class CourseRating(models.Model):
    course_code = models.CharField(max_length=10)
    course_number = models.IntegerField()
    course_name = models.CharField(max_length=255)
    users = models.CharField(max_length=255)
    prof_name = models.CharField(max_length=100)
    textbook_required = models.BooleanField()
    prereq = models.BooleanField()
    delivery = models.CharField(max_length=100)
    review = models.TextField()
    difficulty = models.IntegerField()

    class Meta:
        db_table = 'Rating_course'

    def __str__(self):
        return self.course.course_code + ' ' + self.course.course_number