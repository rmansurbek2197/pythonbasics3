def ortacha_soni_hesobla(sonlar):
    natija = 0
    for son in sonlar:
        natija += son
    ortacha = natija / len(sonlar)
    return ortacha

sonlar_ro_yuqlandi = [1, 2, 3, 4, 5]
print("Sonlar ro'yxati: ", sonlar_ro_yuqlandi)
sonlar_ortachasi = ortacha_soni_hesobla(sonlar_ro_yuqlandi)
print("Sonlar ro'yxati o'rtacha qiymati: ", sonlar_ortachasi)

sonlar_ro_yuqlandi = [10, 20, 30, 40, 50]
print("Sonlar ro'yxati: ", sonlar_ro_yuqlandi)
sonlar_ortachasi = ortacha_soni_hesobla(sonlar_ro_yuqlandi)
print("Sonlar ro'yxati o'rtacha qiymati: ", sonlar_ortachasi)

sonlar_ro_yuqlandi = [100, 200, 300, 400, 500]
print("Sonlar ro'yxati: ", sonlar_ro_yuqlandi)
sonlar_ortachasi = ortacha_soni_hesobla(sonlar_ro_yuqlandi)
print("Sonlar ro'yxati o'rtacha qiymati: ", sonlar_ortachasi)