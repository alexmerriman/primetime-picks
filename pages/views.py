from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Programme
from .forms import ReviewForm

def index(request):
    featured_programmes = Programme.objects.all()[:3]
    context = {
        'featured_programmes': featured_programmes
    }
    return render(request, 'pages/home.html', context)

def programme_list(request):
    programmes = Programme.objects.all()
    context = {
        'programmes': programmes
    }
    return render(request, 'pages/programme_list.html', context)

def programme_detail(request, programme_id):
    programme = get_object_or_404(Programme, id=programme_id)
    reviews = programme.review_set.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.programme = programme
            review.save()
            form = ReviewForm()
    else:
        form = ReviewForm()

    context = {
        'programme': programme,
        'reviews': reviews,
        'form': form
    }
    return render(request, 'pages/programme_detail.html', context)

class ProgrammeCreate(CreateView):
    model = Programme
    template_name = 'pages/programme_form.html'
    fields = ['title', 'genre', 'release_year', 'description', 'image']
    success_url = reverse_lazy('programme_list')

class ProgrammeUpdate(UpdateView):
    model = Programme
    template_name = 'pages/programme_form.html'
    fields = ['title', 'genre', 'release_year', 'description', 'image']
    success_url = reverse_lazy('programme_list')

class ProgrammeDelete(DeleteView):
    model = Programme
    template_name = 'pages/programme_confirm_delete.html'
    success_url = reverse_lazy('programme_list')