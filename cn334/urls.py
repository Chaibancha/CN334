"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ecommerce import views as ecom_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ecommerce/", ecom_views.ecommerce_index_view),
    path("ecommerce/HomePage/<item_id>", ecom_views.home_view),
    path("ecommerce/CategoryPage/<item_id>", ecom_views.category_view),
    path("ecommerce/ProductPage/<item_id>", ecom_views.product_view),
    path("ecommerce/CheckoutPage/<item_id>", ecom_views.checkout_view),
    path("ecommerce/ContactPage/<item_id>", ecom_views.contact_view),
]

