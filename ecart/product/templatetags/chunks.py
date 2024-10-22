from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    """Yields chunks of the list with the given size."""
    for i in range(0, len(list_data), chunk_size):
        yield list_data[i:i + chunk_size]
