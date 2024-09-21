"""Represents an item of equipment."""
class Item():
    def __init__(self, name, cost_cp: int, weight_lbs: int):
        """Creates an instance of this class.

        Args:
          self:
            This object.
          name:
            The name of the item.
          cost_cp:
            The cost of the item in copper pieces.
          weight:
            The weight of the item in pounds.
        """
        self.__name       = name
        self.__cost_cp    = cost_cp
        self.__weight_lbs = weight_lbs    
    
    @property
    def cost_cp(self):
        """The cost of this item in copper pieces."""
        return self.__cost_cp
    
    @property
    def name(self):
        """The name of this item."""
        return self.__name
    
    @property
    def weight_cns(self):
        """The weight of this item in coins."""
        return self.__weight_lbs * 10;
    
    @property
    def weight_lbs(self):
        """The weight of this item in pounds."""
        return self.__weight_lbs;
