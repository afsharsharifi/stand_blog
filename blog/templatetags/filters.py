from django import template

register = template.Library()


@register.filter(name="customtruncate")
def cutter(value, arg):
    return value[:arg]


@register.filter(name="theredigit")
def there_digit_seperator(value):
    return f'{value:,}'
