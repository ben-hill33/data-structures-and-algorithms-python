# Ben Hill
# 5/22/2023

class Client:

    def __init__(self, client_id=0, first_name="Unknown", last_name="Unkown", phone="Unknown", email="Unknown") -> None:
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email

    # classes that compare objects must use __eq__ and __lt__ methods
    def __lt__(self, other) -> bool:
        '''
        __lt__ means "less than" and returns a boolean
        '''
        full_name = self.__last_name + " " + self.__first_name
        other_full_name = other.__last_name + " " + other.__first_name
        return full_name < other_full_name

    def __le__(self, other) -> bool:
        '''
        __le__ means "less than or equal to" and returns a boolean
        '''
        full_name = self.__last_name + " " + self.__first_name
        other_full_name = other.__last_name + " " + other.__first_name
        return full_name <= other_full_name

    def __eq__(self, other: object) -> bool:
        '''
        __eq__ means "equals" and returns a boolean
        '''
        return self.__client_id == other.__client_id

    def __str__(self) -> str:
        '''
        __str__() method is automatically called when you print the object
        '''
        return f"{self.__last_name}, {self.__first_name}"

    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
