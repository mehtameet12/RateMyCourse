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
                row_parts = row[0].split(' ', 1)  # Split on the first space only
                
                if len(row_parts) > 1:
                    # Extract the course code
                    course_code = row_parts[0].strip(' "')
                    
                    # Extract the course number
                    course_number = row_parts[1].strip()
                    
                    if len(course_number) > 4:
                        # Extract the course name if it exists
                        course_name = course_number[4:].strip()
                        course_number = course_number[:4]  # Update course number without the name
                        
            # Create the Course object if all required data is available
            if course_code and course_number and course_name:
                course = Course.objects.create(course_code=course_code, course_number=course_number, course_name=course_name)
                print(f"Created Course object: {course}")
            else:
                print(f"Skipped invalid data: {row}")

