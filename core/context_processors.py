from .models import Contact

def contact_info(request):
    try:
        contact = Contact.objects.first()
    except Exception:
        contact = None

    return {
        'contact': contact,
    }