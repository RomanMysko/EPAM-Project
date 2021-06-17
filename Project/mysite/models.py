from django.db import models


class Price(models.Model):
    """
    model that represents a table of premade prices in a menu.
    consists of 2 fields:
        dish(str):name of dish
        price(float):price of dish
    """
    dish = models.TextField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return str(self.dish) + ":" + str(self.price)


class Order(models.Model):
    """
    model that represents an order table related to Reservation model
    consists of 2 fields:
        dish(str):name of dish
        quantity(int):quantity of dishes
    """
    dish = models.TextField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.dish) + " : " + str(self.quantity)


class Reservation(models.Model):
    """
    model that represents a Reservation object made by a user
    consists of 8 fields:
        date(Date):date of reservation
        time(Time):time of reservation
        party(int):quantity of people attending
        name(str):name of a customer
        email(Email):email address
        phone(int):phone number of a customer
        total_price(float):total price of a reservation
        orders(ManyToManyRelation):ManyToManyRelation to Order class
    """
    date = models.DateField()
    time = models.TimeField()
    party = models.IntegerField()
    name = models.TextField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    total_price = models.FloatField()
    orders = models.ManyToManyField(to=Order)

    def __str__(self):
        return str(self.date) + " : " + str(self.time)
