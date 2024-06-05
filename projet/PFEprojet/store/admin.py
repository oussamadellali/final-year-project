
from .models import Product, Order, OrderItem,Coupon,Payment,User,PaymentChoice
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'street', 'city', 'state', 'country', 'zipcode', 'numberphone')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'street', 'city', 'state', 'country', 'zipcode', 'numberphone'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()

# class UserModelAdmin(BaseUserAdmin):
#   # The fields to be used in displaying the User model.
#   # These override the definitions on the base UserModelAdmin
#   # that reference specific fields on auth.User.
#   list_display = ('id', 'email', 'name', 'is_admin')
#   list_filter = ('is_admin',)
#   fieldsets = (
#       ('User Credentials', {'fields': ('email', 'password')}),
#       ('Personal info', {'fields': ('name',)}),
#       ('Permissions', {'fields': ('is_admin',)}),
#   )
#   # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
#   # overrides get_fieldsets to use this attribute when creating a user.
#   add_fieldsets = (
#       (None, {
#           'classes': ('wide',),
#           'fields': ('email', 'name',  'password1', 'password2'),
#       }),
#   )
#   search_fields = ('email',)
#   ordering = ('email', 'id')
#   filter_horizontal = ()





class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']



class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at', 'ordered']
    list_filter = ['ordered', 'created_at', 'updated_at']
    inlines = [OrderItemInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'discount_price', 'size', 'color', 'category', 'stock']
    list_filter = ['category']
    list_editable = ['price', 'discount_price', 'stock']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [OrderItemInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(PaymentChoice)
admin.site.register(User, UserModelAdmin)