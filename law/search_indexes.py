import datetime
from haystack import indexes
from haystack import site
from law.models import  ProfessionalCategory, Professional, Location


class ProfessionalCategoryIndex(indexes.SearchIndex):
    text = indexes.CharField(use_template=True, document=True)
    title = indexes.CharField(model_attr='name')
    slug = indexes.CharField(model_attr='slug')

    def get_queryset(self):
        "Used when the entire index for model is updated."
        return ProfessionalCategory.objects.filter(creation_date__lte=datetime.datetime.now())

site.register(ProfessionalCategory, ProfessionalCategoryIndex)


class ProfessionalIndex(indexes.SearchIndex):
    text = indexes.CharField(use_template=True, document=True)
    name = indexes.CharField(model_attr='name')
    category = indexes.CharField(model_attr='category')
    slug = indexes.CharField(model_attr='slug')

    def get_queryset(self):
        "Used when the entire index for model is updated."
        return Professional.objects.filter(creation_date__lte=datetime.datetime.now())

site.register(Professional, ProfessionalIndex)




