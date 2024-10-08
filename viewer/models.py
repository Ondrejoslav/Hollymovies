from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, DateTimeField


# Create your models here.

class Genre(Model):
    name = CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f'<Genre: {self.name}>'

    def __str__(self):
        return f'{self.name}'


class Movie(Model):
    objects = None
    title = CharField(max_length=185, null=False, blank=False)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField(null=True, blank=True)
    released = DateField()
    description = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __repr__(self):
        return f'<Movie: {self.title}>'


    def __str__(self):
        return f'{self.title} ({self.released})'
