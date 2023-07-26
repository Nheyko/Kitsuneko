from enum import Enum

Consumable_type = Enum('Consumable_type', ['NONE',
                                            'BUFF',
                                            'HEALING_HEALTH',
                                            'HEALING_HEALTH_AND_MANA',
                                            'HEALING_HEALTH_AND_SKILL',
                                            'HEALING_HEALTH_AND_RAGE',
                                            'HEALING_HEALTH_AND_ENERGY',
                                            'HEALING_MANA',
                                            'HEALING_SKILL',
                                            'HEALING_RAGE',
                                            'HEALING_ENERGY'])