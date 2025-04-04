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
