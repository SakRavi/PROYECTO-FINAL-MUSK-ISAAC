"""
Metodos obligatorios:
            METODO                               FUNCION
    - sales_by_client(client_id)        | todas las ventas de un cliente
    - total_amount_by_client(client_id) | suma de importes de un cliente
    - total_amount_by_category(category)| suma de ventas de una categoria
    - average_sale_by_client(client_id) | media de gasto por venta para un cliente
    
"""
class SalesCollection:

    def __init__(self, sales):
        self.sales = sales

    def sales_by_client(self, client_id):
        client_sales = []
        for sale in self.sales:
            if sale.client_id == client_id:
                client_sales.append(sale)

        return client_sales
    
    def total_amount_by_client(self, client_id):
        total_amount = 0.0
        for sale in self.sales:
            if sale.client_id == client_id:
                total_amount += sale.amount
                
        return total_amount
            
    def total_amount_by_category(self, category):
        total_amount = 0.0
        for sale in self.sales:
            if sale.category == category:
                total_amount += sale.amount

        return total_amount
    
    def average_sale_by_client(self, client_id):
        client_sales = self.sales_by_client(client_id)
        if not client_sales:
            return 0.0

        total_amount = self.total_amount_by_client(client_id)
        average_amount = total_amount / len(client_sales)
        return average_amount
    

