class Account():
    """
    Account class, service and username must be provided to the constructor
    service = str() e.g. Netflix
    username = str() e.g my_email@provider.com
    password = str() eg. myp@ssw_rd
    secure = str() e.g. Verified or Not verified
    """
    def __init__(self,service, username):
        self.service = service
        self.username = username
        self.password = None
        self.secure = "Not verified"
        
        
        
