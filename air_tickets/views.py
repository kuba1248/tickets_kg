from datetime import timezone, datetime

from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .forms import ListingForm
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import AirTic, Order

from .serializers import AirTicSerializer, OrderSerializer
from rest_framework import viewsets


class TicketViewSet(viewsets.ModelViewSet):
    queryset = AirTic.objects.all()
    serializer_class = AirTicSerializer
    # serializeddata = AirTicSerializer(queryset, many=True)

    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    template_name = "index.html"


def index(request):
    assert isinstance(request, HttpRequest)
    queryset = AirTic.objects.all()
    serializer_class = AirTicSerializer(queryset, many=True)
    # serializeddata = AirTicSerializer(queryset, many=True)

    orders = Order.objects.all()

    return render(
        request,
        'index.html',
        {'data': serializer_class.data, 'orders': orders}
    )


def ticket(request, id):
    assert isinstance(request, HttpRequest)
    queryset = AirTic.objects.filter(id=id)
    serializer_class = AirTicSerializer(queryset, many=True)
    # serializeddata = AirTicSerializer(queryset, many=True)

    orders = Order.objects.filter(ticket_id=id)

    if request.POST.get("edit", False):
        return HttpResponseRedirect(reverse("edit_listing", kwargs={"ticket_id": id}))

    if request.POST.get("delete", False):
        messages.success(
            request, f"Your ticket of '{queryset[0].title}' already deleted!")
        queryset.delete()
        return HttpResponseRedirect(reverse("index"))

    return render(
        request,
        'orders.html',
        {'data': serializer_class.data, 'orders': orders}
    )


def edit_listing(request, ticket_id):
    target_listing = AirTic.objects.get(id=ticket_id)

    form = ListingForm(request.POST, request.FILES,
                       instance=target_listing)
    if request.method == "POST":
        if form.is_valid():
            ticket = form.save()
            messages.success(request, f"Edited sucessfully")
            return HttpResponseRedirect(reverse("index"))

    else:
        form = ListingForm(instance=target_listing)

    return render(request, 'edit_listing.html', {'form': form})


def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            form = ListingForm()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ListingForm()

    return render(request, "create_listing.html", {
        "form": form
    })


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
