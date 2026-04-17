from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Programme, Genre
from .forms import ReviewForm
from django.db.models import Avg

def index(request):
    featured_programmes = Programme.objects.all()[:3]
    context = {
        'featured_programmes': featured_programmes
    }
    return render(request, 'pages/home.html', context)

def programme_list(request):
    query = request.GET.get('q')
    genre_id = request.GET.get('genre')

    programmes = Programme.objects.all()
    genres = Genre.objects.all()

    if query:
        programmes = programmes.filter(title__icontains=query)

    if genre_id:
        programmes = programmes.filter(genre_id=genre_id)

    context = {
        'programmes': programmes,
        'query': query,
        'genres': genres,
        'selected_genre': genre_id
    }
    return render(request, 'pages/programme_list.html', context)

def programme_detail(request, programme_id):
    programme = get_object_or_404(Programme, id=programme_id)
    reviews = programme.review_set.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

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
        'form': form,
        'average_rating': average_rating
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