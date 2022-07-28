from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home),
    path('subcategory/<cg_id>/<sub_cg_id>', views.subcategory),
    path('contact_us', views.contact_us),
    path('contact', views.contact),
    path('search', views.search),
    path('contents/<content_id>', views.contentview),
    path('get_subcategories_by_ctid', views.get_subcategories_by_ctid),
    path('get_operting_stuff', views.get_operting_stuff),
]