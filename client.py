import user

class seller(user):
    def __init__(self, name, email, password, id, role):
        super().__init__(name, email, password, id, role)