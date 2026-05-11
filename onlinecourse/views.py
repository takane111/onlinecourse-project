from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission

# Function to handle the exam submission
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Get all choices selected by the user
        selected_choice_ids = [value for key, value in request.POST.items() if 'choice_' in key]
        
        # Create a new submission record
        submission = Submission(course=course)
        submission.save()
        
        # Add the selected choices to the submission
        for choice_id in selected_choice_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
            
        return redirect('onlinecourse:show_exam_result', course_id=course.id)
    