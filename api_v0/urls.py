from django.urls import path, re_path

from .article.views import article_list, category_article_list
from .images.views import gallery_list, images_list
from .files.views import files_list, list_files_list
from .documents.views import documents_list, category_document_list
from .product.views import product_list, category_product_list, products_by_category_list
from .emails.views import email_list
from .personnel.views import personnel_list

urlpatterns = [
    path('articles', article_list),
    path('categories-article', category_article_list),
    path('images', images_list),
    path('gallery', gallery_list),
    path('files', files_list),
    path('lists-files', list_files_list),
    path('documents', documents_list),
    path('category-documents', category_document_list),
    path('products', product_list),
    path('categories-product', category_product_list),
    path('products-by-category', products_by_category_list),
    path('send_email', email_list),
    path('personnel', personnel_list)
]