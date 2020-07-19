from django.utils.safestring import mark_safe
from django.template import Library
import json
import jsonpickle
from django.core.serializers.json import DjangoJSONEncoder

register = Library()


@register.filter(is_safe=True)
def js(obj):
    obj = json.dumps(obj, cls=DjangoJSONEncoder)
    return jsonpickle.encode(obj)
