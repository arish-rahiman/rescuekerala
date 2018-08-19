from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import (InventoryItem, Volunteer, Center, InventoryItemStock, ShipmentRequest, ShipmentRequestItem,
                     InventoryItemCategory, DISTRICTS)


class HomePageView(TemplateView):
    template_name = "supplies_tracker/home.html"


class DistrictListView(ListView, LoginRequiredMixin):
    template_name = "supplies_tracker/list.html"
    model = ShipmentRequest

    def get_queryset(self):
        return ShipmentRequest.objects.filter(delivery_to__district=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(DistrictListView, self).get_context_data(**kwargs)
        context['centers'] = Center.objects.filter(district=self.kwargs['slug'])
        return context


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


class DashBoardView(TemplateView, LoginRequiredMixin):
    template_name = "supplies_tracker/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashBoardView, self).get_context_data(**kwargs)
        district_data = []
        for dis_code, district in DISTRICTS:
            dis_center_data = Center.objects.get_district_center_data(dis_code)
            centers = dis_center_data.get('centers').values_list('id', flat=True)
            dis_request_data = ShipmentRequest.objects.get_district_request_data(centers)
            district_data.append({
                'dis_code': dis_code,
                'name': district,
                'rc_count': dis_center_data['rc_count'],
                'cc_count': dis_center_data['cc_count'],
                'total_requests': dis_request_data['total_requests'],
                'active_requests': dis_request_data['active_requests'],
                'urgent_requests': dis_request_data['urgent_requests'],
            })
        context['district_data'] = district_data
        return context
