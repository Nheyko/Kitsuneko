from enum import Enum

Item_type = Enum('Item_type', ['NONE',
                               'CARD',
                               'COSTUME',
                               'USABLE',
                               'CONSUMABLE',
                               'EQUIPMENT',
                               'MONSTER_EGG',
                               'MOUNT_EGG'
                               'MANA_EGG',
                               'PET_ARMOR',
                               'TAMING_ITEM',
                               'MISCELLANEOUS',
                               'CASH_SHOP',
                               'QUEST'])