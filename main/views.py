from django.shortcuts import render


def show_main(request):
    return render(request, 'main/index.html')


def error404(request, exception):
    return render(request, 'main/404.html', status=404)


def error500(request):
    return render(request, 'main/500.html', status=500)
