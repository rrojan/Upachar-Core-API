from django import template
import json
register = template.Library()


@register.filter
def get(mapping, key):
    return mapping.get(key, '')


@register.filter(name='jsonify')
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)
