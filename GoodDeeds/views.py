from django.views.generic import TemplateView
from django.template.defaulttags import register

from catalog.models import Item, Image, Category

# Create your views here.

class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        last_items = Item.objects.all().order_by('-pub_date')[:10]
        context['last_items'] = last_items

        image_dict : dict = {}
        for item in context['last_items']:
            image_path = None
            for img in Image.objects.filter(item_id=item.id):
                image_path = img.image_path
                break
            if image_path:
                image_dict[item.id] = image_path.name
        context['image_dict'] = image_dict
        
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

