from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import User
from core.forms import AccommodationForm, BookingForm, UpdateAccommodationForm
from core.models import Accommodation, Booking


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


def accommodation_list(request):
    queryset = Accommodation.objects.filter(available=True)
    return render(request,
                  'core/index.html',
                  {'accommodation_object': queryset})


def accommodation_detail(request, pk):
    try:
        accommodation = Accommodation.objects.get(id=pk)
    except accommodation.DoesNotExist:
        raise Http404("No Accommodation found.")
    return render(request,
                  'core/accommodation_detail.html',
                  {'accommodation_object': accommodation})


def accommodation_search(request):
    if request.GET.get('search'):
        query = request.GET.get('search')

        results = Accommodation.objects.filter(Q(city__icontains=query) | Q(num_of_guests__icontains=query))
        return render(request,
                      'core/index.html',
                      {
                          'query': query,
                          'accommodation_object': results})

    if request.GET.get('payment_method'):
        payment_method = request.GET.get('payment_method')

        results = Accommodation.objects.filter(payment_method=payment_method)
        return render(request,
                      'core/index.html',
                      {
                          'query': payment_method,
                          'accommodation_object': results})


@login_required
def booking_accommodation(request, pk):
    if request.method == 'POST':
        # form is sent
        form = BookingForm(request.POST)
        if form.is_valid():
            # form data is valid
            # getting the accommodation object
            accommodation_obj = Accommodation.objects.get(id=pk)
            booking_form = form.save(commit=False)
            # assign current user to the item and accommodation obj
            booking_form.accommodation = accommodation_obj
            booking_form.user = request.user
            booking_form.save()
            messages.success(request,
                             'reservation request sent successfully.')
            # redirect to new created item detail view
            return redirect('/')
    else:
        form = AccommodationForm
    return render(request,
                  'core/create_accommodation.html',
                  {
                      'form': form})


@login_required
def edit_accommodation(request, pk):
    accommodation_obj = Accommodation.objects.get(id=pk)
    if request.method == 'POST':

        update_form = UpdateAccommodationForm(instance=accommodation_obj,
                                              data=request.POST)
        if update_form.is_valid():
            update_form.save()
    else:
        update_form = UpdateAccommodationForm(instance=accommodation_obj)
    return render(request,
                  'core/update_form.html',
                  {'update_form': update_form})


def user_sending_booking_request(request):
    user_obj = User.objects.get(email=request.user.email)
    user_booking_list = user_obj.user_booking.all()
    print(user_booking_list)
    return render(request,
                  'core/user_reservation_request_page.html',
                  {'user_booking_request_data': user_booking_list})


