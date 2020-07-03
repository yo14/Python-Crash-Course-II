# cara1 from geometri.segitiga import hitung_luas_segitiga
# cara1 print(f'hitung_luas_segitiga {hitung_luas_segitiga(10, 3)}')
# cara 2 import geometri.segitiga as gs
# cara 2 print(f'hitung_luas_segitiga {gs.hitung_luas_segitiga(10, 3)}')

from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(10, 3)}')

print(info_persegipanjang())
print(f'hitung_luas_persegi_panjang {hitung_luas_persegi_panjang(10, 3)}')