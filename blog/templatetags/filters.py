from django import template
import datetime
register = template.Library()


@register.filter(name="customtruncate")
def cutter(value, arg):
    return value[:arg]


@register.filter(name="theredigit")
def there_digit_seperator(value):
    return f'{value:,}'


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag('blog/result.html')
def show_result(text):
    return {'text': text}
