from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Regimen, Exercise
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DoingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')

@login_required
def regimens_index(request):
  regimens = Regimen.objects.filter(user=request.user)
  return render(request, 'regimens/index.html', { 'regimens': regimens })

@login_required
def regimens_detail(request, regimen_id):
  regimen = Regimen.objects.get(id=regimen_id)
  doing_form = DoingForm()
  exercises_not_included = Exercise.objects.filter(user=request.user).exclude(id__in = regimen.exercises.all().values_list('id'))
  return render(request, 'regimens/detail.html', {
    'regimen': regimen, 'doing_form': doing_form,
    'exercises': exercises_not_included
   })
  
@login_required
def exercises_index(request):
  exercises = Exercise.objects.filter(user=request.user)
  return render(request, 'exercises/index.html', {'exercises': exercises})  

@login_required
def add_doing(request, regimen_id):
  form = DoingForm(request.POST)
  if form.is_valid():
    new_doing = form.save(commit=False)
    new_doing.regimen_id = regimen_id
    new_doing.save()
  return redirect('detail', regimen_id=regimen_id)

@login_required
def assoc_exercise(request, regimen_id, exercise_id):
  Regimen.objects.get(id=regimen_id).exercises.add(exercise_id)
  return redirect('detail', regimen_id=regimen_id)

@login_required
def assoc_exercise_delete(request, regimen_id, exercise_id):
  Regimen.objects.get(id=regimen_id).exercises.remove(exercise_id)
  return redirect('detail', regimen_id=regimen_id)

class RegimenCreate(CreateView):
  model = Regimen
  fields = ['name', 'muscle_group', 'description', 'days_each_week']
  success_url = '/regimens/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RegimenUpdate(LoginRequiredMixin, UpdateView):
  model = Regimen
  fields = '__all__'

class RegimenDelete(LoginRequiredMixin, DeleteView):
  model = Regimen
  success_url = '/regimens/'

class ExerciseDetail(LoginRequiredMixin, DetailView):
  model = Exercise
  template_name = 'exercises/detail.html'

class ExerciseCreate(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ['name', 'sets', 'reps']
    success_url = '/exercises/'
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class ExerciseUpdate(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ['name', 'sets', 'reps']

class ExerciseDelete(LoginRequiredMixin, DeleteView):
    model = Exercise
    success_url = '/exercises/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid info - please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)