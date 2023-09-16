from django.contrib import admin
from django.urls import path, include
from vege import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name="indexpage"),
    path('contact', views.contact, name="contactus"),
    path('viewRecepies', views.view_rec, name="view_recepies"),
    path('deleteRecepies/<id>/', views.delete_rec, name="delete_recepies"),
    path('updateRecepies/<id>/', views.update_red, name="update_recepies"),
    path('aboutus', views.aboutus, name="abouutus"),
]

admin.site.site_header = "Recepie App Admin"
admin.site.site_title = "Recepie App Admin Portal"
admin.site.index_title = "Welcome to Recepie App"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()