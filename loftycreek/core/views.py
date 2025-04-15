from django.shortcuts import render

# index view
def index(request):
    return render(request, 'core/index.html')

# about view
def about(request):
    return render(request, 'core/about.html')

# academics view
def academics(request):
    return render(request, 'core/academics.html')

# admissions view
def admissions(request):
    return render(request, 'core/admissions.html')

# contact us view
def contact(request):
    return render(request, 'core/contact.html')