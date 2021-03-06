from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete, RichPeopleList, sms
from .views import ProdutoBulk


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('person_list')), name="root"),
    path('list/', PersonList.as_view(), name="person_list"),
    path('rich_list/', RichPeopleList.as_view(), name="rich_list"),
    path('detail/<int:pk>', PersonDetail.as_view(), name="person_detail"),
    path('new/', PersonCreate.as_view(), name="person_new"),
    path('update/<int:pk>/', PersonUpdate.as_view(), name="persons_update"),
    path('delete/<int:pk>/', PersonDelete.as_view(), name="persons_delete"),
    path('produto_bulk/', ProdutoBulk.as_view(), name="produto_delete"),
    path('sms/', sms, name="sms"),
]