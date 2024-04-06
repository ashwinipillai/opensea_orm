from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    twitter_username = models.CharField(max_length=100, blank=True, null=True)


class Collection(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='collections', blank=True, null=True)

    def __str__(self):
        return self.name or 'Unnamed Collection'


class CollectionItem(models.Model):
    collection = models.ForeignKey(Collection, related_name='collection_items', on_delete=models.CASCADE, blank=True,
                                   null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    twitter_username = models.CharField(max_length=100, blank=True, null=True)
    contracts = models.ManyToManyField('Contract', related_name='contract_lists')


class Contract(models.Model):
    address = models.TextField(blank=True, null=True)
    chain = models.TextField(blank=True, null=True)
