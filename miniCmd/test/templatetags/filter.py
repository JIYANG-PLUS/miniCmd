from django import template
import json, re
from collections import Iterable

register = template.Library()

@register.filter
def index(item, i):
    return item[i]

@register.filter
def multiply(item, v):
    return item*v

@register.filter
def split(item, v):
    return item.split(v)

@register.filter
def tojson(item):
    try:
        temp = json.loads(item)
    except:
        return []
    else:
        if isinstance(temp,Iterable):
            return temp
        else:
            return []

@register.filter
def my_in(item, v):
    if v in item: return True
    else: return False

@register.filter
def my_dict(item, v):
    return item[v]
    