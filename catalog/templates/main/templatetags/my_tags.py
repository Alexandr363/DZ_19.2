from django import template

register = template.Library()


@register.filter()
def media_path():
    if val:
        return f'/media/{val}'

    return '#'
