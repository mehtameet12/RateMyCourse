from django.shortcuts import render
from .models import Course


def search_results(request):
    if request.method == 'POST':
        subject_code = request.POST.get('subject_code')
        course_code = request.POST.get('course_code')
        # Perform the search query and retrieve the results
        results = Course.objects.filter(course_code__icontains=subject_code, course_number__icontains=course_code)
        return render(request, 'results.html', {'results': results})
    else:
        return render(request, 'results.html')
