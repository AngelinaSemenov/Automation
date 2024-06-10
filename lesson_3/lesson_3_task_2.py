from smartphone import Smartphone
catalog = [
    Smartphone('Apple', 'Iphone 14', '+79998886655'),
    Smartphone('Samsung', 'Galaxy 50', '+75556667744'),
    Smartphone('Redmi', 'Note 9', '+72223335544'),
    Smartphone('Relmi', '8I', '+5552226655'),
    Smartphone('Honor', '9 Lite', '+75552228883')
]
for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model} {Smartphone.number}")