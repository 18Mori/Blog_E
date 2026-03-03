from .models import *


def get_categories(request):
    categories = Category.objects.all()
    # make sure every category has a slug so templates don’t render "None".
    for cate in categories:
        if not cate.slug:
            from django.utils.text import slugify
            cate.slug = slugify(cate.category_names)
            cate.save(update_fields=['slug'])
    return dict(categories=categories)


def get_social_links(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links=social_links)