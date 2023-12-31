from tabulate import tabulate


class Account():
    """
    Account class contains service, username password and password verification
    self.password attribute including the password itself will be taken
    from password class in the main function
    """

    def __init__(self, service, username):
        self.service = service
        self.username = username
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
