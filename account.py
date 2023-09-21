class Account():
    """
    Account class, service and username must be provided to the constructor
    service = str() e.g. Netflix
    username = str() e.g my_email@provider.com
    """
    def __init__(self,service, username):
        self.service = service
        self.username = username
        self.password = None
        
        
        
