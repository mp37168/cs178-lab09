import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr

REGION = "us-east-1"
TABLE_NAME = "StarbucksDrinks"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_drink(drink):
    name = drink.get("DrinkName", "Unknown")
    size = drink.get("Size", "Unknown")
    price = drink.get("Price", "Unknown")
    print(f"Drink Name: {name}")
    print(f"Size      : {size}")
    print(f"Price     : ${price}")
    print()

def print_all_drinks():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No drinks found in the table.")
        return
    
    print(f"Found {len(items)} drink(s):\n")
    for drink in items:
        print_drink(drink)

def main():
    print("===== Reading Starbucks Drinks Table =====\n")
    print_all_drinks()

if __name__ == "__main__":
    main()