from recipes.models import Tag
from django import template


register = template.Library()



@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def get_tags(request):
    return request.getlist("tag")


@register.filter
def tag_link(request, tag):
    request_copy = request.GET.copy()
    request_copy["page"] = "1"
    tags = request_copy.getlist("tag")
    if tag.title in tags:
        tags.remove(tag.title)
        request_copy.setlist("tag", tags)
    else:
        request_copy.appendlist("tag", tag.title)
    return request_copy.urlencode()


@register.filter
def all_tags(value):
    return Tag.objects.all()


@register.filter
def pagination(request, page):
    request_copy = request.GET.copy()
    request_copy["page"] = page
    return request_copy.urlencode()