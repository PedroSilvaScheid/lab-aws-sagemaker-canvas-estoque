import csv
import random
from datetime import datetime, timedelta

# Configurações
num_products = 20
num_days = 30
initial_stock = 50
min_stock = 10
replenish_stock = 30

# Dados dos produtos
products = [
    ("Cuia", 40.00), 
    ("Erba-mate", 21.00), 
    ("Formaggio Coloniale", 25.00), 
    ("Salame", 20.00),
    ("Vino Bianco", 12.00), 
    ("Bombacha", 8.00), 
    ("Charque", 29.00), 
    ("Spiedo", 27.00),
    ("Coltello", 68.00), 
    ("Farofa", 6.00), 
    ("Succo d'Uva", 5.00), 
    ("Miele", 20.00),
    ("Dolci Fatti in Casa", 14.00), 
    ("Costela", 50.00), 
    ("Grigliata", 75.00), 
    ("Vino Rosso", 30.00),
    ("Formaggio Minas", 28.00), 
    ("Polenta", 10.00), 
    ("Brodo di Carne", 4.00), 
    ("Farina di Grano", 9.00)
]

# Função para gerar uma quantidade inicial de estoque
def generate_initial_stock():
    return {i: initial_stock for i in range(num_products)}

# Função para gerar registros diários
def generate_daily_records(date, stock):
    records = []
    for product_id, (product_name, valor) in enumerate(products):
        quantity_sold = random.randint(1, 5)
        stock[product_id] -= quantity_sold
        
        if stock[product_id] < min_stock:
            # Reposição
            restock_amount = replenish_stock
            stock[product_id] += restock_amount
        
        records.append([product_id + 1, product_name, stock[product_id], valor, date])
    return records

# Gerar dados
with open('estoque.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'product_id', 'product_name', 'quantity', 'valor', 'date'])
    
    start_date = datetime(2024, 8, 1)
    stock = generate_initial_stock()
    record_id = 1
    
    for day in range(num_days):
        date = start_date + timedelta(days=day)
        daily_records = generate_daily_records(date.strftime('%Y-%m-%d'), stock)
        for record in daily_records:
            writer.writerow([record_id] + record)
            record_id += 1