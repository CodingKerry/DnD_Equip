"""Provides functionaility to manipulate monetary values."""
from enum import IntEnum
class CoinType(IntEnum):
    """Enumeration of the types of coins."""
    
    COPPER_PIECE   = 1
    """Represents a copper piece."""
    SILVER_PIECE   = 10
    """Represents a silver piece."""
    ELECTRUM_PIECE = 50
    """Represents an electrum piece."""
    GOLD_PIECE     = 100
    """Represents a gold piece."""
    PLATINUM_PIECE = 1000
    """Represents a platinum piece."""
    
    @staticmethod
    def get_base_coin_type():
        """Gets the base coin type."""
        return CoinType.COPPER
    
    @staticmethod
    def exchange(cp_value: int):
        """Exchanges a number of copper pieces into other coin types.

        Args:
          cp_value (int):
            The value in copper pieces to exchange.

        Returns:
          A dictionary mapping CoinType to the corresponding number of coins. The CoinType.ELECTRUM_PIECE is not used.
        """
        money    = { CoinType.PLATINUM_PIECE: cp_value // CoinType.PLATINUM_PIECE }
        cp_value = cp_value % CoinType.PLATINUM_PIECE
        money[CoinType.GOLD_PIECE] = cp_value // CoinType.GOLD_PIECE
        cp_value = cp_value % CoinType.GOLD_PIECE
        money[CoinType.SILVER_PIECE] = cp_value // CoinType.SILVER_PIECE
        sp       = cp_value // CoinType.SILVER_PIECE
        money[CoinType.COPPER_PIECE] = cp_value % CoinType.SILVER_PIECE
        return money
    
    @staticmethod
    def get_label(cls):
        """Retrieves the label representing a CoinType.

        Args:
          cls:
            The CoinType associated with the label to return.

        Returns:
          The label representing the CoinType.

        Raises:
          ValueError: An unknown value was provided.
        """
        match cls:
            case CoinType.COPPER_PIECE:
                return "cp"
            case CoinType.SILVER_PIECE:
                return "sp"
            case CoinType.ELECTRUM_PIECE:
                return "ep"
            case CoinType.GOLD_PIECE:
                return "gp"
            case CoinType.PLATINUM_PIECE:
                return "pp"
            case _:
                raise ValueError(f"Value \"{cls if cls is not None else 'None'}\" is not a known CoinType.")
