from django.contrib import admin

from core.products.models import Product, Brand, Attribute, \
    AttributeGroup, AttributeConf, ProductImage


class RobotAdmin(admin.ModelAdmin):
    """
    fieldsets = [
        ('General Info', {
            'fields': ['brand', 'name', 'product_type', 'label',
                       'description', 'slug', 'image'],
        }
         ),
        ('FINANCIAL INFO', {
            'fields': ['price', 'discount_price']
        }
         ),
        ('DATASHEET', {
            'fields': ['controller', 'working_range_image', 'number_of_axes',
                       'payload', 'reach',
                       'repeatability', 'picking_cycle', 'mounting', 'weight',
                       ],
            'classes': ('collapse',)
        }
         ),
    ]
    """
    list_display = ['brand',
                    'name',
                    'product_type',
                    ]
    list_display_links = [
        'brand',
        'name',
        'product_type',
    ]
    list_filter = ['brand',
                   'name',
                   'product_type', ]

    search_fields = [
        'name',
        'brand',
    ]


admin.site.register(Product, RobotAdmin)
admin.site.register(Attribute)
admin.site.register(AttributeConf)
admin.site.register(ProductImage)
admin.site.register(AttributeGroup)
admin.site.register(Brand)
