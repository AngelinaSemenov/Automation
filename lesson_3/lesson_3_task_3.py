from mailing import Mailing
from address import Address

# Создание адресов отправителя и получателя

to_address = Address('666666', 'Novosibirsk', 'Lazareva', '22', '25')
from_address = Address('555000', 'Krasnoyarsk', 'Samalova', '85', '76')

# Создание нового отправления

newMailing = Mailing(to_address, from_address, '3696', 850)

# Форматированный вывод информации об отправлении
mailing_info = (
    f'Отправление {newMailing.track} из {newMailing.from_address.index}, '
    f'{newMailing.from_address.city}, {newMailing.from_address.street}, '
    f'{newMailing.from_address.built} - {newMailing.from_address.flat} в '
    f'{newMailing.to_address.index}, {newMailing.to_address.city}, '
    f'{newMailing.to_address.street}, {newMailing.to_address.built} - '
    f'{newMailing.to_address.flat}. Стоимость {newMailing.cost} рублей.'
)
print(mailing_info)