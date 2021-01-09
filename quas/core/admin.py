from django.contrib import admin

from .models import Robot, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile,Brand


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    """
    (Alan belirleme) ("Alan adı- başlık", {'fields':["alanlar (modelde bulunan Fieldlar)}
    fieldsets = [('UUser', {'fields':['user']}),
                 ('ST', {'fields':['street_address']}),
                 ('APP', {'fields': ['apartment_address']}),
                 ('CONT', {'fields': ['country']}),
                 ('zipp', {'fields': ['zip']}),
                 ('address_type', {'fields': ['address_type']}),
                 ('default', {'fields': ['default']}),
                 ]
    """
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

class RobotAdmin(admin.ModelAdmin):
    list_display = ['brand',
                    'title',
                    'category',
                    ]
    list_display_links = [
        'brand',
        'title',
        'category',
    ]
    list_filter = ['brand',
                   'title',
                   'category',]

    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]

admin.site.register(Robot,RobotAdmin)
admin.site.register(Brand)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
