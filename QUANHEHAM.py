
def TAO_DOAN(DIEM1, DIEM2) -> DOANTHANG:
    return DOANTHANG(DIEM1, DIEM2)


def DUONG_GIAO_DUONG(DUONGTHANG1, DUONGTHANG2) -> DIEM:
    return DIEM


def DOAN_GIAO_DOAN(DOANTHANG1, DOANTHANG2) -> DIEM:
    return DIEM


def TIA_GIAO_TIA(TIA1, TIA2) -> DIEM:
    return DIEM


def DUONG_GIAO_DOAN(DUONGTHANG, DOANTHANG) -> DIEM:
    return DIEM


def TIA_GIAO_DOAN(TIA, DOANTHANG) -> DIEM:
    return DIEM


def TIA_GIAO_DOAN(TIA, DOANTHANG) -> DIEM:
    return DIEM


def TIA_GIAO_DUONG(TIA, DUONGTHANG) -> DIEM:
    return DIEM


def HINHCHIEU_DIEM_DUONG(DIEM, DUONGTHANG) -> HINHCHIEU:
    return HINHCHIEU


def HINHCHIEU_DIEM_DOAN(DIEM, DOANTHANG) -> HINHCHIEU:
    return HINHCHIEU


def HINHCHIEU_DIEM_TIA(DIEM, TIA) -> HINHCHIEU:
    return HINHCHIEU


def HINHCHIEU_DUONG_DOAN(DUONGTHANG, DOANTHANG) -> HINHCHIEU:
    return HINHCHIEU


def DODAI(DOANTHANG) -> float:
    return sqrt(abs(DOANTHANG.doanThang1.x - DOANTHANG.doanThang2.x)**2 + abs(DOANTHANG.doanThang1 - DOANTHANG.doanThang2.y)**2)


def DIEM_DOIXUNG_DIEM(DIEM1, DIEM2) -> DIEM:
    return DIEM


def DIEM_DOIXUNG_DUONG(DIEM, DUONGTHANG) -> DIEM:
    return DIEM


def DIEM_DOIXUNG_DOAN(DIEM, DOANTHANG) -> DIEM:
    return DIEM


def DIEM_DOIXUNG_TIA(DIEM, TIA) -> DIEM:
    return DIEM


def GOC_NGOAI(GOC) -> GOC:
    return GOC


def GOC_DOI_DIEN_TAM_GIAC(DOAN) -> DOAN:
    return GOC


def CANH_DOI_DIEN_TAM_GIAC(GOC) -> GOC:
    return
