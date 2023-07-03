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

# class UserCourse(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     #user = models.ForeignKey('User.User', on_delete=models.CASCADE)
#     searched_course_code = models.CharField(max_length=10)
#     searched_course_number = models.CharField(max_length=10)
#     course_name = models.CharField(max_length=255)
#     difficulty = models.IntegerField()
#     prof_name = models.CharField(max_length=100)
#     textbook_required = models.BooleanField()
#     prereq = models.BooleanField()
#     delivery = models.CharField(max_length=100)
#     description = models.TextField()

#     class Meta:
#         db_table = 'Rating_course'

#     def __str__(self):
#         return self.course.course_code + ' ' + self.course.course_number