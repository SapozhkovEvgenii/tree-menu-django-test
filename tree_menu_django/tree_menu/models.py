from django.db import models


from django.db import models
from django.urls import reverse_lazy


class TreeMenu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='child'
    )
    url = models.CharField(max_length=100, unique=True)
    named_url = models.CharField(max_length=100, unique=True)

    def save(self):
        reverse_url = self.url
        named_args = {'url': reverse_url}
        self.url = reverse_lazy('index', kwargs=named_args)
        super(TreeMenu, self).save()

    def __str__(self):
        return self.name


    def get_parents(self):
        if self.parent:
            return self.parent.get_parents() + [self.parent.id]
        else:
            return []

    def get_children(self):
        return self.child.all() # type: ignore
