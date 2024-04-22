from django.urls import path
from catalog.views import CategoriesView, ItemDetailView


urlpatterns = [
    path('', CategoriesView.as_view(template_name='categories_view.html'), name='categories_view'),
    path('<int:pk>/', ItemDetailView.as_view(template_name='item_details.html'), name='item_details'),
]