from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}
NOT_NULLABLE = {
    'blank': False,
    'null': False,
}

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование', **NOT_NULLABLE)
    description = models.CharField(max_length=100, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products', **NULLABLE)
    category_id = models.ForeignKey('Category', on_delete=models.SET_NULL, **NULLABLE)
    price = models.PositiveIntegerField(default=0, **NOT_NULLABLE)
    creation_date = models.DateTimeField(auto_now_add=True, **NOT_NULLABLE)
    changed_date = models.DateTimeField(auto_now=True, **NOT_NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)


class Category(models.Model):
    name = models.CharField(max_length=50, **NOT_NULLABLE)
    description = models.TextField(**NULLABLE)
    created_at = models.CharField(max_length=50, **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)