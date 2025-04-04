from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.
def popular_course_list(request):
    context = {}

    if request.method == 'GET':
        # Use object model to read all courses and sort by enrollment.
        course_list = Course.objects.order_by('-total_enrollment')[:10]

        # Add course list as an entry in the context, to be picked up by templates.
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)

def enroll(request, course_id):
    if request.method == 'POST':
        # First, read course object. If not found, raise 404
        course = get_object_or_404(Course, pk=course_id)

        course.total_enrollment += 1
        course.save()

        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

def course_details(request, course_id):
    context = {}

    if request.method == 'GET':
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            # Use render() method to make an HTML page w/ Template and context

            return render(request, 'onlinecourse/course_detail.html', context)
        except Course.DoesNotExist:
            # If course doesn't exist, throw HTTP404 error
            raise Http404("No Course matches the given ID.")
