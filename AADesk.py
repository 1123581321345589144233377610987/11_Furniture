import AAOfficeFurniture


class Desk(AAOfficeFurniture.OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, number_drawers, location_drawers):
        self.__number_drawers = number_drawers
        self.__location_drawers = location_drawers
        AAOfficeFurniture.OfficeFurniture.__init__(self, category, material, length, width, height, price)

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def set_location_drawers(self, location_drawers):
        self.__location_drawers = location_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def get_location_drawers(self):
        return self.__location_drawers

    def __str__(self):
        return f"\nCategory: {self.get_category()}\nMaterial: {self.get_material()}\nLength: {self.get_length()}\nWidth: {self.get_width()}\nHeight: {self.get_height()}\nPrice: {self.get_price()}\nNumber of Drawers: {self.__number_drawers}\nLocation of Drawers: {self.__location_drawers}"
