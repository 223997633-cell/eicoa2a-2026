def calc_power(voltage,resistance):
    """ Calculate power using Ohm's Law.
    Args:
    voltlate=(float) voltage across component in volts.
    Resistance=(float) Resistance if a component in Ω .

    Returns:
     float
          Power in watts(W)
           
    """
    current=voltage/resistance
    return voltage*current
