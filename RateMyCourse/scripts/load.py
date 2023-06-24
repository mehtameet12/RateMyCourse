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

        # Delete existing Course objects
        Course.objects.all().delete()

        print("Deleted existing Course objects")

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the course code, course number, and course name
            course_code, course_number, course_name = None, None, None

            if len(row) >= 3:
                # Extract the course code, course number, and course name from the row
                course_code = row[0]
                course_number = row[1]
                course_name = row[2].split(" (")[0]

            # Create the Course object if all required data is available
            if course_code and course_number and course_name:
                # Print the course data in the desired format
                course_data = f"{course_code} {course_number} {course_name}"
                print(course_data)

                # Create the Course object
                course = Course.objects.create(
                    course_code=course_code, course_number=course_number, course_name=course_name
                )
                print(f"Created Course object: {course.course_code}, {course.course_number}, {course.course_name}")
            else:
                print(f"Invalid data: {row}")