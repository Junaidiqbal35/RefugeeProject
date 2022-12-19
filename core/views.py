from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DetailView, ListView

from core.forms import AccommodationForm
from core.models import Accommodation


@login_required
def accommodation_create(request):
    if request.method == 'POST':
        # form is sent
        form = AccommodationForm(request.POST)
        if form.is_valid():
            # form data is valid
            accommodation_form = form.save(commit=False)
            # assign current user to the item
            accommodation_form.user = request.user
            accommodation_form.save()
            messages.success(request,
                             'Accommodation added successfully')
            # redirect to new created item detail view
            return redirect('/')
    else:
        form = AccommodationForm
    return render(request,
                  'core/create_accommodation.html',
                  {
                      'form': form})


class AccommodationList(LoginRequiredMixin, ListView):
    template_name = "core/index.html"
    queryset = Accommodation.objects.filter(available=True)
    context_object_name = 'accommodation_object'
    model = Accommodation


class CreateAccommodationView(LoginRequiredMixin, CreateView):
    model = Accommodation
    form_class = AccommodationForm
    template_name = 'core/create_accommodation.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')


class AccommodationDetailView(DetailView):
    template_name = "core/accommodation_detail.html"
    queryset = Accommodation.objects.all()
    context_object_name = 'accommodation_object'
    slug_field = 'pk'
    model = Accommodation
