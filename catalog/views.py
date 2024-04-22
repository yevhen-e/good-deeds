from django.views.generic import ListView, DetailView, TemplateView
from django.template.defaulttags import register

from catalog.models import Category, Item, Image

# Create your views here.

class CategoriesView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        context['categories'] = categories

        countItemsByCategories : dict = {}
        for category in categories:
            if Item.objects.filter(category_id = category.id):
                countItemsByCategories[category.id] = len(Item.objects.filter(category_id = category.id))
            else:
                countItemsByCategories[category.id] = 0
        context['countItemsByCategories'] = countItemsByCategories

        return context


    @register.filter
    def get_dict_value(dictionary, key):
        return dictionary.get(key)
    

class CatalogListView(ListView):
    model = Item
    paginate_by = 15
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_dict : dict = {}
        itemsListByCategory : list
        if context['view'].kwargs:
            itemsListByCategory = Item.objects.filter(category_id = context['view'].kwargs['category_id'])
            context['item_list'] = itemsListByCategory

        for item in context['item_list']:
            image_path = None
            for img in Image.objects.filter(item_id=item.id):
                image_path = img.image_path
                break
            if image_path:
                image_dict[item.id] = image_path.name

        context['image_dict'] = image_dict
        return context
    
    @register.filter
    def get_dict_value(dictionary, key):
        return dictionary.get(key)


class ItemDetailView(DetailView):
    model = Item
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.filter(item_id=context['item'].id)
        context['images'] = images
        return context
    
