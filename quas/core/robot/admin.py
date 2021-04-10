from django.contrib import admin

from core.robot.models import Robot, Axis, Brand, Controller
from core.users.models import UserProfile

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class RobotAxis(admin.TabularInline):
    model = Axis
    extra = 0
    classes = ('collapse',)
class RobotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Info', {
            'fields': ['brand', 'title', 'category', 'label', 'description',
                       'slug', 'image'],
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
            'fields': ['controller', 'working_range_image', 'number_of_axes', 'payload', 'reach',
                       'repeatability', 'picking_cycle', 'mounting', 'weight', 'axis'],
            'classes': ('collapse',)
        }
         ),
    ]
    list_display = ['brand',
                    'title',
                    'category',
                    'performance_rating',
                    ]
    list_display_links = [
        'brand',
        'title',
        'category',
        'performance_rating',
    ]
    list_filter = ['brand',
                   'title',
                   'category', ]

    search_fields = [
        'title',
        'brand',
    ]
    actions = [make_refund_accepted]


admin.site.register(Robot, RobotAdmin)
admin.site.register(Axis)
admin.site.register(Brand)
admin.site.register(Controller)
"""
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)

'axis1_speed', 'axis1_movement', 'axis2_speed', 'axis2_movement',
                       'axis3_speed', 'axis3_movement', 'axis4_speed', 'axis4_movement', 'axis5_speed', 'axis5_movement',
                       'axis6_speed','axis6_movement'
"""
