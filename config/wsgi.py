"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()



#####
def home(request):
    products = Product.objects.all()
    return render(request, 'online_shop/home.html',  {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'online_shop/detail.html', {'product': product})
