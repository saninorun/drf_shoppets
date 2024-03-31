from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from pytils.translit import slugify

from products.managers import CatalogManager


# Create your models here.


class Category(MPTTModel):
    title = models.CharField(max_length=250, verbose_name="Наименование", unique=True)
    description = models.TextField(verbose_name="Описание категории", blank=True)
    slug = models.SlugField(verbose_name="URL", unique=True, blank=True, null=True)
    image = models.ImageField(
        verbose_name="Фотография", upload_to="category/%Y%m%d/", blank=True
    )
    parent = TreeForeignKey(
        to="self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Родительская категория",
    )

    class MPTTMeta:
        order_insertion_by = ("title",)

    class Meta:
        unique_together = ("title", "slug")
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Дополнение родительского метода сохранения модели в базу данных,
        в случае отсутствия значения переменной 'slug' при заполнении поля модели.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название", unique=True)
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(verbose_name="URL", unique=True, blank=True, null=True)
    image = models.ImageField(
        verbose_name="Фотографии", upload_to="products/%Y%m%d/", blank=True, null=True
    )
    accounting_unit = models.CharField(max_length=15, verbose_name="Единица хранения")
    manufacturer = models.CharField(max_length=250, verbose_name="Производитель")
    article_number = models.IntegerField(verbose_name="Артикул", blank=True, null=True)
    categories = TreeForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        related_name="items",
        verbose_name="Категория",
    )

    objects = models.Manager()
    catalog_manager = CatalogManager()

    class Meta:
        ordering = ("title",)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Дополнение родительского метода сохранения модели в базу данных,
        в случае отсутствия значения переменной 'slug' при заполнении поля модели.
        """

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
