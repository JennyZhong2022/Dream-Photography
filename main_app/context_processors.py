# context_processors.py in your Django app

def photographer_check(request):
    is_photographer = request.user.is_authenticated and request.user.groups.filter(name='Photographer').exists()
    return {'is_photographer': is_photographer}

def client_check(request):
    is_client = request.user.is_authenticated and request.user.groups.filter(name='Client').exists()
    return {'is_client': is_client}