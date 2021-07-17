from django.contrib import admin

from core.products.models import Product, Brand, Controller, Attribute, \
    AttributeGroup, RobotClass


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class RobotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Info', {
            'fields': ['brand', 'title', 'product_type', 'label',
                       'description', 'slug', 'image'],
        }
         ),
        ('FINANCIAL INFOS', {
            'fields': ['price', 'discount_price']
        }
         ),
        ('RATINGS', {
            'fields': ['performance_rating', 'customer_rating']
        }),
        ('APPLICATION', {
            'fields': ['application'],
            'classes': ('collapse',),
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
    list_display = ['brand',
                    'title',
                    'product_type',
                    'performance_rating',
                    ]
    list_display_links = [
        'brand',
        'title',
        'product_type',
        'performance_rating',
    ]
    list_filter = ['brand',
                   'title',
                   'product_type', ]

    search_fields = [
        'title',
        'brand',
    ]
    actions = [make_refund_accepted]


admin.site.register(Product, RobotAdmin)
admin.site.register(RobotClass)
admin.site.register(Attribute)
admin.site.register(AttributeGroup)
admin.site.register(Brand)
admin.site.register(Controller)

