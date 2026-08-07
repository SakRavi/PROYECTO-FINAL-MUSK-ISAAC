import csv
import json
from pathlib import Path

import pandas as pd

# Import Files (prp.)
from src.client import Client
from src.client_collection import ClientCollection
from src.functional_utils import (
    filter_sales_by_category,
    filter_sales_by_client,
    sales_to_dict,
    total_sales_amount,
)
from src.sale import Sale
from src.sales_collection import SalesCollection

# = = = = = = = = = = = = = 

# Root (files)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SHORT_ROOT = PROJECT_ROOT.name

CLIENTS_FILE = PROJECT_ROOT / "data" / "clients.json"
SHORT_ROOT_C = CLIENTS_FILE.name

SALES_FILE = PROJECT_ROOT / "data" / "sales.csv"
SHORT_ROOT_S = SALES_FILE.name

# ! testing
def print_file_true_test():
    print(f"Project root: {PROJECT_ROOT.exists()} | {SHORT_ROOT}/")
    print(f"Clientes file: {CLIENTS_FILE.exists()} | data/{SHORT_ROOT_C}")
    print(f"Ventas file: {SALES_FILE.exists()} | data/{SHORT_ROOT_S}")
    print(f"Clientes file: {CLIENTS_FILE.read_text()}")
    print(f"Clientes file: {SALES_FILE.read_text()}")

# = = = = = = = = = = = = = 

# Cargas datos
def load_clients():
    with CLIENTS_FILE.open("r", encoding="utf-8") as file:
        json_reader = json.load(file)

        list_clients = []

        for client_record in json_reader:
            client_obj = Client(
                client_id=int(client_record["client_id"]),
                name=client_record["name"].strip(),
                country=client_record["country"].strip(),
                signup_date=client_record["signup_date"].strip(),
            )
            list_clients.append(client_obj)
            
    return list_clients

def load_sales():
    with SALES_FILE.open("r",encoding="utf-8",newline="",) as file:
        csv_reader = csv.DictReader(file)
        
        list_sales = []
        
        for sale_record in csv_reader:
            sale_obj = Sale(
                sale_id=sale_record["sale_id"],
                client_id=sale_record["client_id"],
                product=sale_record["product"],
                category=sale_record["category"],
                amount=sale_record["amount"],
                date=sale_record["date"],
            )

            list_sales.append(sale_obj)
            
    return list_sales

# TEST 
def test_type_format_sales():

    list_sales = load_sales()

    for sale_obj in list_sales:
        print("sale_id:", sale_obj.sale_id, type(sale_obj.sale_id))
        print("client_id:", sale_obj.client_id, type(sale_obj.client_id))
        print("product:", sale_obj.product, type(sale_obj.product))
        print("category:", sale_obj.category, type(sale_obj.category))
        print("amount:", sale_obj.amount, type(sale_obj.amount))
        print("date:", sale_obj.date, type(sale_obj.date))

        break
    
# carga listas
list_clients = load_clients()
list_sales = load_sales()

# colecciones class
client_collection = ClientCollection(list_clients)
sales_collection = SalesCollection(list_sales)

# = = = = = = = = = = = = = 
# ! 10 calculos
# 1. (n) Total de Clientes
def count_total_clients(list_clients):
    total_clients = len(list_clients)
    return total_clients
    
def test_01():
    total_clients = count_total_clients(list_clients)
    print("1 .(n) Total de Clientes")
    print(total_clients)
    
# 2. (n) Total de Ventas
def count_total_sales(list_sales):
    total_sales = len(list_sales)
    return total_sales
    
def test_02():
    total_sales = count_total_sales(list_sales)
    print("2. (n) Total de Ventas")
    print(total_sales)
    
# 3. Total Ingr. x Cliente
def calculate_total_spent_by_client(client_id, sales_collection):
    total_spent = sales_collection.total_amount_by_client(client_id)
    return total_spent

def test_03():
    print("3. Total Ingr. x Cliente")
    for client_obj in list_clients:
        total_spent = calculate_total_spent_by_client(client_obj.client_id,sales_collection,)
        print(client_obj.name,"->",round(total_spent, 2),)

# 4. (n) Ventas x (Cliente)
def count_sales_by_client(client_id, sales_collection):
    client_sales = sales_collection.sales_by_client(client_id)
    total_client_sales = len(client_sales)
    return total_client_sales

def test_04():
    print("4. (n) Ventas x (Cliente)")
    for client_obj in list_clients:
        sale_count = count_sales_by_client(client_obj.client_id,sales_collection,)
        print(client_obj.name,"->",sale_count,)
        
# 5. Ingr. Prom. x (Venta de Cliente)
def calculate_average_sale_by_client(client_id, sales_collection):
    average_sale = sales_collection.average_sale_by_client(client_id)
    return average_sale

def test_05():
    print("5. Ingr. Prom. x (Venta de Cliente)")
    for client_obj in list_clients:
        average_sale = calculate_average_sale_by_client(client_obj.client_id,sales_collection,)
        print(client_obj.name,"->",round(average_sale, 2),)
        
# 6. Mayor Gasto x Pais (Cliente)
def find_top_client_by_country(list_clients,client_collection,sales_collection,):
    countries = []
    for client_obj in list_clients:
        if client_obj.country not in countries:
            countries.append(client_obj.country)
    top_client_by_country = {}
    
    for country in countries:
        country_clients = client_collection.clients_by_country(country)
        top_client_name = None
        top_total_spent = 0.0
        for client_obj in country_clients:
            total_spent = sales_collection.total_amount_by_client(client_obj.client_id)
            if total_spent > top_total_spent:
                top_total_spent = total_spent
                top_client_name = client_obj.name
        top_client_by_country[country] = top_client_name
        
    return top_client_by_country

def test_06():
    top_client_by_country = find_top_client_by_country(list_clients,client_collection,sales_collection,)
    print("6. Mayor Gasto x Pais (Cliente)")
    print(top_client_by_country)
    
# 7. Total Ventas x (categoria)
def calculate_sales_by_category(list_sales):
    sales_dataframe = pd.DataFrame(sales_to_dict(list_sales))
    sales_by_category = (sales_dataframe.groupby("category")["amount"].sum().round(2).to_dict())
    return sales_by_category

def test_07():
    sales_by_category = calculate_sales_by_category(list_sales)
    print(" 7. Total Ventas x (categoria)")
    print(sales_by_category)
    
# 8. Cliente +Ventas (categoria especifica)
def find_top_client_by_category(list_clients,list_sales,category,):
    category_sales = filter_sales_by_category(list_sales,category,)

    top_client_name = None
    top_sale_count = 0

    for client_obj in list_clients:
        client_category_sales = filter_sales_by_client(category_sales,client_obj.client_id,)
        sale_count = len(client_category_sales)
        if sale_count > top_sale_count:
            top_sale_count = sale_count
            top_client_name = client_obj.name

    return top_client_name

def test_08():
    top_electronics_client = find_top_client_by_category(list_clients,list_sales,"Electronics",)
    print("8. Cliente +Ventas (categoria especifica)")
    print(top_electronics_client)
    
# 9. (n) clientes superan (Gasto minimo)
def find_high_spending_clients(list_clients,sales_collection,minimum_spent=500,):
    high_spending_clients = []

    for client_obj in list_clients:
        total_spent = sales_collection.total_amount_by_client(client_obj.client_id)
        if total_spent > minimum_spent:
            high_spending_clients.append(client_obj.name)

    return high_spending_clients

def test_09():
    high_spending_clients = find_high_spending_clients(list_clients,sales_collection,500,)
    print("9. (n) clientes superan (Gasto minimo)")
    print(high_spending_clients)
    
# 10. Ventas acum. (Mes-A-Mes)
def calculate_monthly_sales(list_sales):
    sales_dataframe = pd.DataFrame(sales_to_dict(list_sales))
    sales_dataframe["date"] = pd.to_datetime(sales_dataframe["date"])
    sales_dataframe["month"] = (sales_dataframe["date"].dt.strftime("%Y-%m"))
    monthly_sales = (sales_dataframe.groupby("month")["amount"].sum().round(2).to_dict())

    return monthly_sales

def test_10():
    monthly_sales = calculate_monthly_sales(list_sales)
    print("10. Ventas acum. (Mes-A-Mes)")
    print(monthly_sales)
    
# = = = = = = = = = = = = = 
# ! REPORT

def generate_report():
    
    total_clients = count_total_clients(list_clients) #1
    total_sales = count_total_sales(list_sales) #2
    
    clients_report = []
    for client_obj in list_clients:
        total_spent = calculate_total_spent_by_client(client_obj.client_id,sales_collection,) #3
        sale_count = count_sales_by_client(client_obj.client_id,sales_collection,) #4
        average_sale = calculate_average_sale_by_client(client_obj.client_id,sales_collection,) #5

        client_data = {
            "client_id": client_obj.client_id,
            "name": client_obj.name,
            "total_spent": round(total_spent, 2),
            "sale_count": sale_count,
            "average_sale": round(average_sale, 2),
        }
        clients_report.append(client_data)

    top_client_by_country = find_top_client_by_country(list_clients,client_collection,sales_collection,) # 6
    sales_by_category = calculate_sales_by_category(list_sales)# 7
    
    # !
    top_electronics_client = find_top_client_by_category(list_clients,list_sales,"Electronics",) # 8
    top_accessories_client = find_top_client_by_category(list_clients, list_sales, "Accessories",) # 8
    # !
    high_spending_clients = find_high_spending_clients(list_clients,sales_collection,500,) # 9
    monthly_sales = calculate_monthly_sales(list_sales)# 10
    
    # reporte final
    total_revenue = round(total_sales_amount(list_sales), 2)
    report = {
        "summary": {
            "total_clients": total_clients,
            "total_sales": total_sales,
            "total_revenue": total_revenue,
        },
        "clients": clients_report,
        "top_client_by_country": top_client_by_country,
        "sales_by_category": sales_by_category,
        "high_spending_clients": high_spending_clients,
        "monthly_sales": monthly_sales,
    }

    return report

def test_m_report():
    report = generate_report()
    print(report["summary"])
    for client_data in report["clients"]:
        print(client_data)

# ! JSON  REPORT

def save_report_json(report):

    output_file = PROJECT_ROOT / "report.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(report,file, indent=4, ensure_ascii=False)
        
    return output_file

# !python -m pytest
# !python -m src.analyze
if __name__ == "__main__":
    
    report = generate_report()
    save_report_json(report)
