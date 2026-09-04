def cm_to_inches(cm):
    """Convert centimeters to inches.
    Args:
         Length in centimeters
    Returns:
            float length in inches(1 inches=2.54cm)  

    """
    return cm/2.54


def inches_to_cm(inches):
    """Convert inches to centimeters.
    Args:
          inches(float):Length in centimetes
    Returns:
            float:length in centimeters(inches*2.54)
    """
    return inches*2.54 

def mm_to_inches(mm):
    """ Convert millimeters to inches.
    Args:
         Length in  millimeters.
    Returns:
            float: Length in inches (1 inch=25.4 mm)

    """
    return mm/25.4

def inches_to_mm(inches):
 """Convert inches to millimeters.
Args:
     inhes(float): Length in millimeters.
Returns:
        float: Length in millimeters (inches*25.4)

 
 """
 return inches * 25.4


if __name__ == "__Conversion__":
   print("cm_to_inches:" , cm_to_inches(15))
   print("inches_to_cm:",inches_to_cm(2))
