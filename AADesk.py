import AAOfficeFurniture

class Desk(AAOfficeFurniture.OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, number_drawers, location_drawers):
        AAOfficeFurniture.OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__number_drawers = number_drawers
        self.__location_drawers = location_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def set_location_drawers(self, location_drawers):
        self.__location_drawers = location_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def get_location_drawers(self):
        return self.__location_drawers

    def __str__(self):
        return f"\nCategory: {AAOfficeFurniture.OfficeFurniture.get_category}\nMaterial: {Desk.get_material}\nLength: {Desk.get_length}\nWidth: {Desk.get_width}\nHeight: {Desk.get_height}\nPrice: {Desk.get_price}\nNumber of Drawers: {Desk.get_number_drawers}\nLocation of Drawers: {Desk.get_location_drawers}"