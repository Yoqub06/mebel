from django.contrib import admin
from django.utils.html import format_html
from .models import Color, Cart, Category, User, MebelImage, Mebel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'slug', 'get_img']
    list_display_links = ['id', 'name']
    readonly_fields = ['slug', 'id']

    @admin.display(empty_value="---", description="Image")
    def get_img(self, obj):
        return format_html(f"""
        <img src="{obj.image.url}" style="max-width: 150px;">
        """)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.StackedInline):
    extra = 1
    model = MebelImage


@admin.register(Mebel)
class MebelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ctg', 'show_price', 'img']
    list_display_links = ['id', 'name']

    inlines = [ImageInline]
    fieldsets = [
        ("General", {"fields": ["ctg", "name"]}),
        ("Price", {"fields": ["price", "price_type", "discount"]}),
        ("Qo'shimcha", {"fields": ["color", "material", "filled", "extra"]}),
        ("Rasmer", {"fields": ["g_length", "g_width", "g_height", "is_spalniy", "s_length", "s_width", "s_height"]}),
    ]

    @admin.display(empty_value="---", description="Mebel Image")
    def img(self, obj):
        img = obj.first_image()
        if obj.first_image():
            return format_html(f"""
            <img src="{img}" style="max-width: 150px;">
            """)

        return "---"

    @admin.display(empty_value="---", ordering="price")
    def show_price(self, obj):
        if obj.discount:
            return format_html(f"""
            <del style="color: red; font-size: 12px;">{obj.price:,}</del> {self.discount}% OFF<br>
            <span style="color: green; font-size: 16px;">{obj.get_price():,} {obj.get_type()}</span>
            """)
        return f"{obj.get_price():,}"

    show_price.short_description = "Narxi"


@admin.display(empty_value="---", description="O'lchamlari")
def spalniy(self, obj):
    if obj.is_spalniy:
        return format_html(f"""
                    <h5>Gabarit o'lcham</h5>
                    <div> class="size-item"> Uzunlik: <mark>{obj.g_length}</mark></div>
                    <div> class="size-item"> Kenglik: <mark>{obj.g_width}</mark></div>
                    <div> class="size-item"> Balandlik: <mark>{obj.g_height}</mark></div><br>
                    
                    <h5>Spalniy o'lcham</h5>
                    <div> class="size-item"> Uzunlik: <mark>{obj.s_length}</mark></div>
                    <div> class="size-item"> Kenglik: <mark>{obj.s_width}</mark></div>
                    <div> class="size-item"> Balandlik: <mark>{obj.s_height}</mark></div><br>

        """)

    return format_html(f"""
                    <h5>Gabarit o'lcham</h5>
                    <div> class="size-item"> Uzunlik: <mark>{obj.g_length}</mark></div>
                    <div> class="size-item"> Kenglik: <mark>{obj.g_width}</mark></div>
                    <div> class="size-item"> Balandlik: <mark>{obj.g_height}</mark></div><br>
    """)
