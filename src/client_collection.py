"""
Metodos obligatorios:
                METODO                          FUNCION
        - get_client_by_id(id)          | devuelve un client concreto
        - clients_by_country(country)   | devuelve lista de cliente de un pais
"""
class ClientCollection:
    
    def __init__(self, clients):
        self.clients = clients
        
    def get_client_by_id(self, id):
        for client in self.clients:
            if client.client_id == id:
                return client
                
        return None
        
    def clients_by_country(self, country):
        country_clients = []
            
        for client in self.clients:
            if client.country == country:
                country_clients.append(client)
                    
        return country_clients


