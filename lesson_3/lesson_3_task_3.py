from mailing import Mailing
from address import Address


to_address = Address('666666', 'Novosibirsk', 'Lazareva', '22', '25')
from_address= Address('555000', 'Krasnoyarsk', 'Samalova', '85', '76')
newMailing = Mailing (to_address, from_address,'3696', 850)
print(f'Отправление {newMailing.track} из {newMailing.from_address.index}, {newMailing.from_address.city}, {newMailing.from_address.street}, {newMailing.from_address.built} - {newMailing.from_address.flat} в {newMailing.to_address.index}, {newMailing.to_address.city}, {newMailing.to_address.street}, {newMailing.to_address.built} - {newMailing.to_address.flat}. Стоимость {newMailing.cost} рублей.')