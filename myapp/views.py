import calendar
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from datetime import date, datetime, timedelta
from hitcount.views import HitCountDetailView
from django.utils.safestring import mark_safe
from django.contrib import messages
from .utils import Calendar
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .models import Post, Reply, Notification, Activities, Meeting, Health, Shopping, Attendees

from .forms import ActivityReplyForm, CreateActivityForm, CreateMeetingForm, CreateUserForm, FileForm, ReplyForm


@login_required(login_url='login')
def home(request):
    context = {
        'posts': Post.object.all()
    }
    return render(request, 'myapp/home.html', context)

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context['url'] = fs.url(name)
    return render(request, 'myapp/upload.html', context)

def activity(request):
    activity_list = Activities.objects.all()
    return render(request, 'myapp/activity.html',
    {'activity_list': activity_list})

def health(request):
    health_list = Health.objects.all()
    return render(request, 'myapp/health.html',
    {'health_list': health_list})

def shopping(request):
    shopping_list = Shopping.objects.all()
    return render(request, 'myapp/shopping.html',
    {'shopping_list': shopping_list})

def shoppingDetail(request):
    data = Shopping.objects.values('item_category').annotate(quantity=Sum('quantity'))
    context = {
        "data": data,
    }

    return render(request, 'myapp/shopping_detail.html', context)

def meeting(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'myapp/meeting.html',
    {'meeting_list': meeting_list})

def attendees(request):
    attendees = Attendees.objects.all()
    return render(request, 'myapp/meeting.html',
    {'attendees': attendees})

class PostListView(ListView):
    model = Post
    template_name = 'myapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(HitCountDetailView, DetailView):
    model = Post
    count_hit = True

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/home/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ReplyCreateView(CreateView):
    model = Reply
    form_class =  ReplyForm
    template_name = 'myapp/reply_create.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = '/home/'

class PostNotification(View):
    def get(self, request, notification_pk, post_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        post = Post.objects.get(pk=post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('post-detail', pk=post_pk)

class DeleteNotification(View):
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)

        notification.user_has_seen = True
        notification.save()

        HttpResponse('Success', content_type='text/plain')

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'myapp/login.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'myapp/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def makeActivity(request):
    form = CreateActivityForm()

    if request.method == 'POST':
        form = CreateActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity')
    context = {'form':form}
    return render(request, 'myapp/activity_form.html', context)

def makeMeeting(request):
    form = CreateMeetingForm()

    if request.method == 'POST':
        form = CreateMeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting')
    context = {'form':form}
    return render(request, 'myapp/meeting_form.html', context)

def activityDetailView(request):
    activities = Activities.objects.get(pk=1)
    context = {'activities': activities}
    return render(request, 'myapp/activity_detail.html', context)

class ActivityReplyCreateView(CreateView):
    model = ActivityReply
    form_class = ActivityReplyForm
    template_name = 'myapp/reply_create.html'
    
    def form_valid(self, form):
        form.instance.activities_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = '/activity/'

class ActivityListView(ListView):
    model = Activities
    template_name = 'myapp/activity.html'
    context_object_name = 'activities'
    ordering = ['-pk']

class ActivityDetailView(HitCountDetailView, DetailView):
    model = Activities
    count_hit = True

class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activities
    fields = ['author', 'name', 'type', 'startTime', 'endTime', 'location', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    success_url = '/activity/'

class CalendarView(ListView):
    model = Activities
    template_name = 'myapp/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        #d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        
        
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context 

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def showfile(request):
    lastfile = File.objects.last()
    form = FileForm(request.POST or None, request.FILES or None)
    
    if lastfile is not None:    
        filepath = lastfile.filepath
        filename = lastfile.name
        context = {
            'filepath':filepath,
            'filename':filename,
            'form':form
        }
    else:
        context = {
            'form':form
        }
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'myapp/upload.html', context)

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
