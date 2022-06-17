def deteksi_kata(kalimat,kata):
    kalimat = kalimat.split()
    identifikasi = False
    for idx,value in enumerate(kalimat):
        if value == kata:
            print(f"Kata '{kata}' berada di kata ke-{idx+1} pada kalimat ini.")
            identifikasi = True
        else :
            continue
    if identifikasi != True:
        print(f"Kata '{kata}' tidak terdapat pada kalimat ini.")

        
kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dicari: ")
deteksi_kata(kalimat,kata)