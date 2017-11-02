class Product(object):
    def __init__(self, item_name, price, tax, weight, brand, status):
        self.item_name = item_name
        self.price = price
        self.tax = tax
        self.total_price = self.price * self.tax + self.price
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sold(self):
        self.status = "The {} have been sold!".format(self.item_name)
        return self
    def display_info(self):
        print "Item Name: {}. Price: ${}. Tax: {}. Total Price ${}. Weight: {}  - lbs. Brand: {}. Status: {}".format(self.item_name, self.price, self.tax, self.total_price, self.weight, self.brand, self.status)
        return self
    def return_item(self, reason, box_status):
        self.status = reason
        self.box_status = reason
        if self.box_status is "defective":
            self.price = 0
            self.tax = 0
            self.total_price = 0
            self.status = "Defective. Not for sale"
        elif self.box_status == "in box":
            self.status = "Like New!"
        elif self.box_status == "opened box":
            self.price = self.price * .8
            self.status = "Used: 20% discount!"
        else:
            self.price = self.price * .8
            self.status = "Used: 20% discount!"
        return self

product1 = Product("Cheerios", 10, 0.1, 1, "General Mills", "test")
product1.return_item("Didn't like", "defective" )
product1.display_info()

#still need to add tax and total price adjustments to in box and used areas.