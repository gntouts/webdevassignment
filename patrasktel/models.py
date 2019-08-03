from django.db import models

# Create your models here.


class Route(models.Model):
    """Model representing a Route"""
    name = models.CharField(
        max_length=200, help_text='''Enter the route's name''')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Ticket(models.Model):
    ZONE_CATEGORY = [
        ('A', 'Zone A'),
        ('B', 'Zone B'),
    ]
    PRICE_CATEGORY = [
        ('n', 'Normal Price'),
        ('r', 'Reduced Price'),
    ]
    source = models.CharField(
        max_length=150, help_text='''Enter the photo's source URL''',)
    zone = models.CharField(
        max_length=1, choices=ZONE_CATEGORY, default='A', help_text='''Enter A for local or B for intercity''',)
    price_cat = models.CharField(
        max_length=1, choices=PRICE_CATEGORY, default='n', help_text='''Enter Normal or Reduced''',)
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False, default='0.0',
                                help_text='''Enter the price of the ticket''',)
    customer = models.TextField(
        max_length=100, help_text='''Enter the eligible social categories''')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.zone} {self.price_cat} {self.value} '


class Stop(models.Model):
    """Model representing a Stop"""
    ZONE_CATEGORY = [
        ('a', 'Zone A'),
        ('b', 'Zone B'),
    ]
    name = models.CharField(
        max_length=150, help_text='''Enter the stop's name''')

    zone = models.CharField(
        max_length=1, choices=ZONE_CATEGORY, default='a', help_text='''Enter A for local or B for intercity''',)
    number = models.IntegerField(
        help_text='''Which stop is it? E.g Fisrt Stop is number 1 etc''')
    route = models.ForeignKey('Route', default='1',
                              on_delete=models.CASCADE,
                              )

    class Meta:
        ordering = ['number']
        unique_together = ("route", "name")

    def getZone(self):
        '''Returns the zone the stop belongs to'''
        return self.zone

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Schedule(models.Model):
    '''Model representing the starting time of each route'''
    route = models.ForeignKey('Route', on_delete=models.CASCADE,)
    start_time = models.TimeField()

    class Meta:
        unique_together = ("route", "start_time")

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.route}, {self.start_time}'


class About(models.Model):
    source = models.CharField(
        max_length=150, help_text='''Enter the photo's source URL''',)

    text = models.TextField(
        max_length=2500, default="a", help_text='''Enter the main body of the announcement''')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} About'


class Contact(models.Model):
    phone = models.CharField(
        max_length=13, help_text='''Enter the company's phone number''',)
    email = models.EmailField(
        help_text='''Enter the company's phone number''',)

    address = models.CharField(
        max_length=100, help_text='''Enter the company's address''',)

    class Meta:
        ordering = ['-id']

    def get_url(self):
        return f'https://maps.google.com/maps?q={self.address}&t=&z=15&ie=UTF8&iwloc=&output=embed'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.phone} {self.email} {self.address}'


class Announcement(models.Model):
    heading = models.CharField(
        max_length=200, help_text='''Enter the title of the announcement''')
    author = models.CharField(
        max_length=100, help_text='''Enter the author of the announcement''')
    date = models.DateTimeField()
    body = models.TextField(
        max_length=2000, help_text='''Enter the main body of the announcement''')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.heading} {self.date}'
