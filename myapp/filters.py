from .models import *
import django_filters
from django import forms


class cpuFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.NumberFilter(lookup_expr='lte')  # lte 小於  gte 大於
    chip = django_filters.NumberFilter(lookup_expr='gte',)


class hddFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class ssdFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class displayFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class chassisFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class MBFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class MemoryFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class PowerFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')


class ALLFilter(django_filters.FilterSet):
    name_all = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class Meta:
    model = cpu, display, hdd, ssd, chassis, MB, Memory, Power, All
    fields = '__all__'
