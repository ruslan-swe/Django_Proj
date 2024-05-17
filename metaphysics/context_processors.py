from .models import Contacts

def contact_details(request):
    contact_details = Contacts.objects.first()
    return {'contact_details': contact_details}