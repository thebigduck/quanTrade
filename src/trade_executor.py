def execute_trade(action, amount, price):
    """
    Simulates trade execution by printing the action.
    """
    total_cost = amount * price
    print(f"Executing {action} order for {amount} shares at ${price:.2f}. Total cost: ${total_cost:.2f}")
