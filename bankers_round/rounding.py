from decimal import Decimal, ROUND_HALF_EVEN

def bankers_round(value):
    """
    Banker's rounding: Round-half-to-even.
    Always round to 2 decimal places.
    """
    # Use repr() to get a more precise float string representation
    d = Decimal(repr(value))
    return float(d.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN))