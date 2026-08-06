# CLASS CLIENT

class Client:

    def __init__(self, client_id: int, name: str, country: str, signup_date: str):
        
        self.client_id = client_id
        self.name = name
        self.country = country
        self.signup_date = signup_date
        
    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "country": self.country,
            "signup_date": self.signup_date
        }

# PRE_TESTING
if __name__ == "__main__":
    client = Client(
        client_id=1,
        name="Alice",
        country="Spain",
        signup_date="2022-03-15",
    )
    print(client.to_dict())

