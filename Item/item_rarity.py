from enum import Enum

Item_type = Enum('Item_type', ['NONE',
                               'VERY_COMMON',
                               'COMMON',
                               'UNCOMMON',
                               'RARE',
                               'VERY_RARE',
                               'EPIC',
                               'LEGENDARY'
                               'ABYSSAL'])