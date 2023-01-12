from django.db import models


class Menu(models.Model):
    CHILD = 'CHD'
    PARENT = 'PRT'

    MENU_TYPES = (
        (CHILD, 'категория'),
        (PARENT, 'родительская_категория'),
    )

    category = models.CharField(max_length=25, choices=MENU_TYPES)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='menu')

    def __str__(self):
        return "<Menu: {}>".format(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'