from django import template

# Register the custom filters
register = template.Library()

@register.filter
def round_value(value):
    """
    Custom filter to round a number to the nearest integer.
    """
    try:
        return round(value)
    except (ValueError, TypeError):
        return value

@register.filter
def percentage(value, total):
    """
    Custom filter to calculate the percentage of `value` out of `total`.
    """
    try:
        if total == 0:
            return 0  # Avoid division by zero
        return (value / total) * 100
    except (ValueError, TypeError):
        return 0


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, 0)