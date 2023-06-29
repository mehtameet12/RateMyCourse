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