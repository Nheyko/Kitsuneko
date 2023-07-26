from enum import Enum

Element = Enum('Element', ['NONE'
                           
                           'NEUTRAL',
                           'POISON',
                           'GHOST',
                           'UNDEAD',

                           'SHADOW',
                           'DUSK',
                           'DARKNESS',
                           'VOID',

                           'PHOTON',
                           'LIGHT',
                           'HOLY',
                           'DIVIN'
                           
                           'WATER', # Water
                           'AQUA', # Water + 1
                           'RAIN', # Water + 2
                           'LAKE', # Water + 3

                           'EARTH', # Earth
                           'STONE', # Earth + 1
                           'QUAKE', # Earth + 2
                           'GRAVITY', # Earth 3 

                           'FIRE', # Fire
                           'FLARE', # Fire + 1
                           'BLAZE', # Fire + 2
                           'VOLCANO', # Fire + 3

                           'WIND', # Wind
                           'GUST', # Wind + 1
                           'CYCLONE', # Wind + 2
                           'TEMPEST', # Wind + 3

                           'LIGHTNING', # Wind / Fire
                           'THUNDER', # Gust / Flare
                           'STORM', # Cyclone / Blaze

                           'BLIZZARD', # Water / Wind
                           'FROST', # Aqua / Gust
                           'ICICLE', # RAIN / CYCLONE

                           'FOREST', # Earth / Water
                           'LEAF', # Stone / Aqua
                           'TREE', # Quake / Rain

                           'EXPLOSION', # Fire / Earth
                           'BOMB', # Flare / Stone
                           'BLAST', # Blaze / Quake

                           'LIFE', # Fire / Earth / Water / Wind
                           'HEAL', # # Aqua / Stone / Flare / Gust
                           'BURST', # Fire / Earth / Water / Wind
                           'BOOSTER', # Aqua / Stone / Flare / Gust

                           'CALAMITY', # Volcano / Quake
                           'FOREST', # Gravity / Rain
                           'BLIZZARD', # Lake / Cyclone
                           'PHOTON', # Tempest / Blaze

                           'CLUSTER', # Volcano / Gravity
                           'HOLY', # Gravity / Lake
                           'FENRIR', # Lake / Tempest
                           'CHAOS', # Tempest + Volcano

                           'HOLY', # Water / Earth / Forest
                           'DIVIN',
                           'CHAOS', # Fire / Wind / Lightning
                           'MIST', # Wind / Water / Blizzard
                           'GRAVITY', # Earth / Fire / Explosion
                           'SOUL', # Wind / Water / Lightning

                           'FAIRY', # Defensive
                           'DRAGON', # Offensive

                           'DUST', # Magic lvl 0
                           'ETHER', # Volcano / Gravity / Lake / Tempest

                           'SKY',
                           'STAR', # Lightning / Explosion
                           'ASTRAL',
                           'VOID',
                           'OMBRAL',
                           'TWILIGHT',

                           'LAVA',
                           'HEAT',
                           'MIST',
                           'SQUALL',
                           'SAND',
                           'RAINBOW',

                           'BLOOD'])