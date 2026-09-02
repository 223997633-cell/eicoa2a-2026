def calc_resistance(voltage,current):
    """
    Calculate electrical resistance using Ohm's law.
    
    Args:
        voltage(float): Voltage across the component in volts(V).
        Current(float): Current through the component in amperes(A). Must be non-zero.

    Retuns:
    float
         resistance in ohms(Ω).
    Notes:
          the function raises a ZerodivisionError if cuurent is ).
    """
    return voltage/ current