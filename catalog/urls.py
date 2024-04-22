from django.urls import path
from catalog.views import CatalogListView, CategoriesView, ItemDetailView


urlpatterns = [
    # path('', CatalogListView.as_view(template_name='items_list.html'), name='items_list'),
    path('', CategoriesView.as_view(template_name='categories_view.html'), name='categories_view'),
    path('<int:pk>/', ItemDetailView.as_view(template_name='item_details.html'), name='item_details'),
]