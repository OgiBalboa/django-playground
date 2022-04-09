from django.conf.urls import url, include

from core.api.resources.routers import CatalogRouter

from core.products.views import ProductView, AttributeView

catalog_router = CatalogRouter()

catalog_router.register(r'products', ProductView)
catalog_router.register(r'attributes', AttributeView)

urlpatterns = [
    url(r'^v1/catalog/', include(catalog_router.urls)),
]