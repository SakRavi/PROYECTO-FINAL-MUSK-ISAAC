"""
ATRIBUTOS:
    - sale_id:(id unico de la venta (int)) **
    - client_id:(clave externa)
    - product:(Nombre del producto vendido)
    - category:(categ. (Electronics,....))
    - amount:(Importe de la venta)
    - date:(fecha de la venta (str))
METODO:
    - to_dict()
    
!JORGE: sale_id: pdf indica INT, datos/Pytest usan STR
! bash: python -m src.analyze
! ValueError: invalid literal for int() with base 10: 'S1001'
"""

class Sale:
    
    def __init__(self,sale_id,client_id,product,category,amount,date):
        
        self.sale_id = str(sale_id)  # INT PDF -> CSV/Pytest usan STR
        self.client_id = int(client_id)
        self.product = str(product)
        self.category = str(category)
        self.amount = float(amount)
        self.date = str(date)
        
    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "client_id": self.client_id,
            "product": self.product,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }
        
