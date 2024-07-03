from django.http import HttpResponse

# Create your views here.

def home_page(request):
    if request.method == 'GET':
        return HttpResponse('The HOME page')
    else:
        pass

def user_page(request):
    return HttpResponse('The user page')

def user_register(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        return login, password
    else:
        return HttpResponse('The register page')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return username, password
    else:
        return HttpResponse('The login page')