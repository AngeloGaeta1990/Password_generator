from tabulate import tabulate


class Account():
    """
    Account class, service and username must be provided to the constructor
    service = str() e.g. Netflix
    username = str() e.g my_email@provider.com or user
    password = str() eg. myp@ssw_rd
    secure = str() e.g. Verified or Not verified
    """

    def __init__(self, service, username):
        self.service = service
        self.username = username
        self.password = None
        self.secure = "Not verified"

    def print_account(self):
        """
        Prints account info into a tabular format
        """
        table_data = self.account_dict()
        table = tabulate(table_data.items(), headers="firstrow",
                         tablefmt="grid")
        return table

    def account_dict(self):
        return {
            'Account': self.service,
            'User': self.username,
            'Password': self.password,
            'Password security': self.secure
        }
