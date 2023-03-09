# Desarrollar un ejemplo para rendondeo inferior y superior

import math
print(math.floor(1.568 * 100) / 100) # Redondeo hacia abajo 1.568 * 100 ==> 156.8 / 100 = 1.56
print(math.floor(1.168 * 100) / 100) # Redondeo hacia abajo

"""
1.25584878964564
1.26 # Arriba
1.25 # Abajo
1.25 # Corta
"""

print(math.ceil(1.568 * 100) / 100) # Redondeo hacia arriba
print(math.ceil(1.168)) # Redondeo hacia arriba