import csv 
import os
from Results.models import Course

def run():
    file = os.path.join(os.path.dirname(__file__), 'course_data.csv')
    #file = open('course_data.csv', 'r')
    read_file = csv.reader(file)

    Course.objects.all().delete()

    count = 1

    for course in read_file:
        if count ==1:
            pass
        else:
            course_code = course[0]
            course_number = course[1]
            course_name = course[2]
            Course.objects.create(course_code=course_code, course_number=course_number, course_name=course_name)
        count += 1

