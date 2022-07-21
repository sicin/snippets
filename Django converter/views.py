from django.shortcuts import render
import copy

from .forms import *
from .scripts.units_converter import unit_conversion
from .scripts.numbers_converter import converter_main
from .scripts.reverse_numbers_converter import reverse_converter_main
from .scripts.sexagenary_converter import sexagenary_main
from .scripts.time_converter import time_main


converter_html = 'converter/converter.html'

modules = {
    "values":
    {'mass': {'form': UnitConverterMass(), 'data': "", 'error': ""},
     'length': {'form': UnitConverterLength(), 'data': "", 'error': ""},
     'volume': {'form': UnitConverterVolume(), 'data': "", 'error': ""},
     'area': {'form': UnitConverterArea(), 'data': "", 'error': ""},
     'numbers': {'form': NumbersConverter(), 'data': "", 'error': ""},
     'reverse_numbers': {'form': ReverseNumbersConverter(), 'data': "", 'error': ""},
     'sexagenary': {'form': SexagenaryConverter(), 'data': "", 'error': ""},
     'time': {'form': TimeConverter(), 'data': "", 'error': ""},
     'combo': {'form': ComboConverter(), 'data': "", 'error': ""},
     }
}
modules_clear = copy.deepcopy(modules)


def converter_page(request):
    modules["values"] = copy.deepcopy(modules_clear["values"])
    return render(request, converter_html, modules)


def generic_converter(request, measurement: str):
    # modules["values"][measurement]["error"] = ""
    user_input = request.POST.get('value')
    system_presplit = request.POST.get(f'{measurement}_system')
    try:
        module, period, unit = system_presplit.split('|')
    except AttributeError:
        modules["values"] = copy.deepcopy(modules_clear["values"])
        return render(request, converter_html, modules)
    else:
        modules["values"][measurement]["data"] = unit_conversion(
            user_input, module, period, unit)
        return render(request, converter_html, modules)


def mass(request):
    return generic_converter(request, "mass")


def length(request):
    return generic_converter(request, "length")


def volume(request):
    return generic_converter(request, "volume")


def area(request):
    return generic_converter(request, "area")


def complex_converter(request, script_used, conversion_type: str):
    # modules["values"]["numbers"]["error"] = ""
    user_input = request.POST.get('value')
    try:
        modules["values"][conversion_type]["data"] = script_used(user_input)
    except TypeError:
        modules["values"] = copy.deepcopy(modules_clear["values"])
        return render(request, converter_html, modules)
    else:
        return render(request, converter_html, modules)


def numbers(request):
    return complex_converter(request, converter_main, "numbers")


def sexagenary(request):
    return complex_converter(request, sexagenary_main, "sexagenary")


def complex_converter_choice(request, script_used, conversion_type: str):
    # modules["values"]["numbers"]["error"] = ""
    user_input = request.POST.get('value')
    choice = request.POST.get(f'{conversion_type}_system')
    try:
        modules["values"][conversion_type]["data"] = script_used(
            user_input, choice)
    except (TypeError, AttributeError):
        modules["values"] = copy.deepcopy(modules_clear["values"])
        return render(request, converter_html, modules)
    else:
        return render(request, converter_html, modules)


def reverse_numbers(request):
    return complex_converter_choice(request, reverse_converter_main, "reverse_numbers")


def time(request):
    return complex_converter_choice(request, time_main, "time")


def combo(request):
    return render(request, converter_html, modules)
