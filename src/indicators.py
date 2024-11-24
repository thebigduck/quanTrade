# src/indicators.py

def calculate_total_sell_volume(order_book_data, levels=5):
    """
    Calculates the total sell volume from the top levels of the order book.

    Parameters:
        order_book_data (dict): Order book data containing 'asks'.
        levels (int): Number of top levels to consider.

    Returns:
        float: Total sell volume.
    """
    asks = order_book_data['asks'][:levels]
    total_sell_volume = sum(ask['size'] for ask in asks)
    return total_sell_volume

def calculate_sell_to_buy_ratio(order_book_data, levels=5):
    """
    Calculates the ratio of total sell volume to total buy volume.

    Parameters:
        order_book_data (dict): Order book data containing 'bids' and 'asks'.
        levels (int): Number of top levels to consider.

    Returns:
        float: Sell-to-buy volume ratio.
    """
    asks = order_book_data['asks'][:levels]
    bids = order_book_data['bids'][:levels]
    total_sell_volume = sum(ask['size'] for ask in asks)
    total_buy_volume = sum(bid['size'] for bid in bids)
    if total_buy_volume == 0:
        return float('inf')
    return total_sell_volume / total_buy_volume

def calculate_order_book_imbalance(order_book_data, levels=5):
    """
    Calculates the order book imbalance between buy and sell orders.

    Parameters:
        order_book_data (dict): Order book data containing 'bids' and 'asks'.
        levels (int): Number of top levels to consider.

    Returns:
        float: Order book imbalance ranging from -1 to 1.
    """
    asks = order_book_data['asks'][:levels]
    bids = order_book_data['bids'][:levels]
    total_ask_size = sum(ask['size'] for ask in asks)
    total_bid_size = sum(bid['size'] for bid in bids)
    if total_bid_size + total_ask_size == 0:
        return 0
    imbalance = (total_bid_size - total_ask_size) / (total_bid_size + total_ask_size)
    return imbalance
