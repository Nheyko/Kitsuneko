from enum import Enum

Equipment_location = Enum('Equipment_location', ['NONE',
                                                 'HAT_UPPER',
                                                 'HAT_MIDDLE',
                                                 'HAT_LOWER',
                                                 'NECK'
                                                 'SHOULDERS',
                                                 'WRIST',
                                                 'GLOVES',
                                                 'LEFT_HAND',
                                                 'RIGHT_HAND',
                                                 'CHEST',
                                                 'WAIST',
                                                 'GARMENT'
                                                 'LEGS',
                                                 'FEET',
                                                 'LEFT_EARRING',
                                                 'RIGHT_EARRING',
                                                 'LEFT_RING',
                                                 'RIGHT_RING',
                                                 'BACK', # Capes
                                                 'SPECIAL']) # Echo of Soul comme le quiver pour l'archer etc