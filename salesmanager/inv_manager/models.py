from django.db import models



class Category(models.Model):
    """
        The category class represents a category of it's associated
        product, it helps with organization.
    """
    name = name = models.CharField("Nombre", max_length=20)



class Storage(models.Model):
    """
        The storage class represents a storage place of the shop.
    """

    name = models.CharField("Nombre", max_length=20)
    refrigerated = models.BooleanField("Refrigerado")
    restricted = models.BooleanField("Restringido")


class Product(models.Model):
    """
        The product class is the main class within the whole project.
        It describes a product in the real shop.
    """

    name = models.CharField("Nombre", max_length=20, default="producto")
    qty = models.IntegerField("Cantidad", default=0)
    category = models.ForeignKey(verbose_name="Categoría", to=Category, on_delete=models.SET_DEFAULT, default=None)
    cost = models.IntegerField("Costo", default=0)
    price = models.IntegerField("Precio", default=0)
    storage_place = models.ForeignKey(verbose_name="Lugar de almacenado", to=Storage, on_delete=models.SET_DEFAULT, default=None)

    @property
    def expected_earning(self):
        """
            Return the expected earning for the 
            products price with respect to it's cost
        """
        return int(self.price - self.cost)
