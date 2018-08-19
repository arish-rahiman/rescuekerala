from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import (InventoryItem, Volunteer, Center, InventoryItemStock, ShipmentRequest, ShipmentRequestItem,
                     InventoryItemCategory)





class HomePageView(TemplateView):
    template_name = "supplies_tracker/home.html"


class UpdateShipmentRequestView(UpdateView, LoginRequiredMixin):
    model = ShipmentRequest
    template_name = 'supplies_tracker/update_request.html'
    fields = [
        'id',
        'status'
    ]

    def get_success_url(self):
        return reverse("supplies_tracker:update_request", kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(UpdateShipmentRequestView, self).get_context_data(**kwargs)
        context['items'] = ShipmentRequestItem.objects.filter(shipment_request=self.object)
        return context