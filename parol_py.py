def uzunlik_tekshir(parol):
    return len(parol) >= 8


def kuchli_parol(parol):
    if len(parol) < 8:
        return False

    katta_harf = False
    kichik_harf = False
    raqam = False

    for belgi in parol:
        if belgi.isupper():
            katta_harf = True
        elif belgi.islower():
            kichik_harf = True
        elif belgi.isdigit():
            raqam = True

    return katta_harf and kichik_harf and raqam
