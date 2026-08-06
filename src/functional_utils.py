from functools import reduce


def filter_sales_by_category(sales, category):
    return list(filter(lambda sale: sale.category == category, sales))

def filter_sales_by_client(sales, client_id):
    return list(filter(lambda sale: sale.client_id == client_id, sales))

def sales_to_dict(sales):
    return list(map(lambda sale: sale.to_dict(),sales))  # noqa: C417

def total_sales_amount(sales):
    return reduce(lambda total, sale: total + sale.amount, sales, 0.0)
