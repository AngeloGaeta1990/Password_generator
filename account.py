class Account():
    """
    Account class, service and username must be provided to the constructor
    service = str() e.g. Netflix
    username = str() e.g my_email@provider.com
    password = str() eg. myp@ssw_rd
    secure = bool() e.g. True or False
    """
    def __init__(self,service, username):
        self.service = service
        self.username = username
        self.password = None
        self.secure = None
        
        
        
