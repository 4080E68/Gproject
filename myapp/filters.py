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
    thread = django_filters.NumberFilter(lookup_expr='gte',)
    


class hddFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    size = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(choices=(('', '請選擇尺寸'),) + hdd.GENRE_CHOICES,attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')
    capacity_TB = django_filters.NumberFilter(lookup_expr='gte',)
    


class ssdFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')
    size = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(choices=(('', '請選擇尺寸'),) + ssd.GENRE_CHOICES, attrs={'class': 'form-control'}))
    capacity_TB = django_filters.NumberFilter(lookup_expr='gte',)
    read_speed_mbs = django_filters.NumberFilter(lookup_expr='gte',)
    write_speed_mbs = django_filters.NumberFilter(lookup_expr='gte',)


class displayFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')
    Memory = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(choices=(('', '請選擇記憶體'),) + display.GENRE_CHOICES, attrs={'class': 'form-control'}))


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
    foot_position_MB = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(choices=(('', '請選擇適用類型'),) + MB.GENRE_CHOICES, attrs={'class': 'form-control'}))


class MemoryFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')
    type = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.Select(choices=(('', '請選擇適用類型'),) + Memory.GENRE_CHOICES, attrs={'class': 'form-control'}))
    clock_rate = django_filters.NumberFilter(lookup_expr='gte',)
    capacity_GB = django_filters.NumberFilter(lookup_expr='gte',)


class PowerFilter(django_filters.FilterSet):
    vendor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='lte')
    Watts = django_filters.NumberFilter(lookup_expr='gte',)


class ALLFilter(django_filters.FilterSet):
    name_all = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class Meta:
    model = cpu, display, hdd, ssd, chassis, MB, Memory, Power, All
    fields = '__all__'
