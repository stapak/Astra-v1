"""
This file is to keep a track of all user defined exeception.
"""

class NotAuthorized(Exception):
    """
    This execption   used to raise error when some user uses the method for which they are not permitted.
    """
    pass

class TreatmentComplete(Exception):
    """ 
    This exeception is used when some user tries to edit patient details who is not a patient anymore.
    """
    pass

class UserDetailsNotFound(Exception):
    """
    This error used to indicate that the user mention is not found in the database.
    """
    pass