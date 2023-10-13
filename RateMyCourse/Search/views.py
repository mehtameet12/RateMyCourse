from django.shortcuts import render

# Create your views here.
from .models import Course, CourseRating

def search_results(request):
    if request.method == 'GET':
        subject_code = request.GET.get('subject_code')
        course_code = request.GET.get('course_code')
        # Perform the search query and retrieve the results
        results = Course.objects.filter(course_code__icontains=subject_code, course_number__icontains=course_code)
        ratings = CourseRating.objects.filter(course_code__icontains=subject_code, course_number__icontains=course_code)
        return render(request, 'results.html', {'results': results, 'ratings': ratings} )
    else:
        return render(request, 'results.html')


