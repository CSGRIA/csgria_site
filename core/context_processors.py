from .models import Contact


def contact_info(request):
    """Injecte les infos de contact dans tous les templates."""
    try:
        contact = Contact.objects.first()
    except Exception:
        contact = None

    return {
        'contact': contact,
    }