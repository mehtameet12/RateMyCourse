import csv
import os
from Results.models import Course

def run():
    file = os.path.join(os.path.dirname(__file__), 'course_data.csv')
    
    print(f"CSV file path: {file}")
    
    # Open the CSV file
    with open(file, 'r') as csvfile:
        # Create a CSV reader
        reader = csv.reader(csvfile)
        
        # Skip the header row
        next(reader)
        
        # Delete existing Course objects
        Course.objects.all().delete()
        
        print("Deleted existing Course objects")
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the course code, course number, and course name
            course_code, course_number, course_name = None, None, None
            
            if row:
                # Extract the course code, course number, and course name from the row
                course_parts = row[0].split(',"')  # Split on ',"' to separate the description
                
                if len(course_parts) > 1:
                    # Extract the course code
                    course_code = course_parts[1].split()[0]
                    
                    # Extract the course number
                    course_number = course_parts[1].split()[1]
                    
                    # Extract the course name without units
                    course_name = course_parts[0].strip('"')
                        
            # Create the Course object if all required data is available
            if course_code and course_number and course_name:
                course = Course.objects.create(course_code=course_code, course_number=course_number, course_name=course_name)
                print(f"Created Course object: {course.course_code},{course.course_number},{course.course_name.split('(')[0].strip()}")
            else:
                print(f"Skipped invalid data: {row}")
