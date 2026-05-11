from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission

# Function to handle the exam submission
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Logic to calculate score and create a Submission object would go here
        return redirect('onlinecourse:show_exam_result', course_id=course.id)
    return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})

# Function to show the result after submission
def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Logic to fetch the latest submission for the user
    return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})