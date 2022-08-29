from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class News(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=150)
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    public_date = models.DateTimeField()

    def get_tag(self):
        tags_li = self.tag.all()
        res = []
        for tag in tags_li:
            res.append(tag.title)
        return ', '.join(res)

    def __str__(self):
        return self.title
