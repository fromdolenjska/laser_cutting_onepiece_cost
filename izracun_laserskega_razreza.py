obseg_kosa_zunanja_kontura = int(input("Vpiši obseg zunanje konture kosa: \n")) #mm



obseg_lukenj = 200 #mm
stevilo_prebojev = 5
offset_material_1kos = 450 #mm
čas_preboja = 1.5 #sekunda
hitrost_razreza_zun_kontura = 50 #mm/s
hitrost_razreza_not_kontura = 20 #mm/s

def cas_izreza_kosa():
    cas_zun_kon = obseg_kosa_zunanja_kontura // hitrost_razreza_zun_kontura #posamezne spremenljivke lahko znotraj funkcije tudi printađ da ves kaksni so delni rezultati
    cas_not_kon = obseg_lukenj // hitrost_razreza_not_kontura * stevilo_prebojev
    cas_prebojev = stevilo_prebojev * čas_preboja
    return cas_zun_kon + cas_not_kon + cas_prebojev
print("To je cas celotnega razreza kosa ", cas_izreza_kosa()) # ne das vmes plus ker int in str ne mores sestevat ampak das vejico (,)
