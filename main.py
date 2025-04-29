# from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

# print(get_mask_card_number(1234123412341234))
# print(get_mask_account(12341234123412341234))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(get_date("2024-03-11T02:26:18.671407"))
