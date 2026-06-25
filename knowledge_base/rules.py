RULES = {

    "Gastritis (Maag)": {

        "kode": "P01",

        "gejala": {
            "G01": 0.9,   # Nyeri ulu hati
            "G16": 0.8,   # Nyeri perut
            "G12": 0.7,   # Mual
            "G11": 0.7,   # Muntah
            "G17": 0.6,   # Perut kembung
            "G22": 0.6,   # Nafsu makan berkurang
            "G20": 0.6,   # Cepat kenyang
            "G21": 0.5,   # Sendawa berlebihan
            "G25": 0.5    # Keringat dingin
        },
        
        "onset": {
            "<1 minggu": 0.4,
            "1-4 minggu": 0.7,
            ">1 bulan": 0.9
        },
        
        "riwayat": {
            "Gastritis": 0.9,
            "GERD": 0.4,
            "Dispepsia": 0.5,
            "Tukak Lambung": 0.3,
            "Gastroenteritis": 0.2,
            "Lainnya": 0.0,
            "Tidak": 0.0
        },

        "deskripsi":
        """
        Gastritis (maag) adalah peradangan pada dinding
        lambung yang dapat menyebabkan nyeri ulu hati,
        mual, muntah, dan gangguan pencernaan lainnya.
        """,

        "solusi": [
            "Makan secara teratur",
            "Hindari telat makan",
            "Kurangi makanan pedas dan asam",
            "Kelola stres",
            "Perbanyak minum air putih",
            "Istirahat yang cukup"
        ],
        
        "obat": [
            "Antasida", 
            "Sukralfat*", 
            "Omeprazole*", 
            "Lansoprazole*"
        ],

        "pantangan": [
            "Makanan pedas",
            "Makanan asam",
            "Kopi",
            "Makanan instan",
            "Minuman bersoda"
        ]
    },

    "GERD": {

        "kode": "P02",

        "gejala": {

            "G03": 0.9,   # Dada terasa panas
            "G04": 0.8,   # Rasa asam/pahit di mulut
            "G05": 0.8,   # Tenggorokan terasa panas
            "G06": 0.9,   # Makanan naik kembali
            "G07": 0.8,   # Sulit menelan
            "G08": 0.6,   # Batuk kering
            "G09": 0.6,   # Napas sesak
            "G24": 0.3,   # Demam
            "G12": 0.6    # Mual
        },
        
        "onset": {
            "<1 minggu": 0.4,
            "1-4 minggu": 0.7,
            ">1 bulan": 0.9
        },
        
        "riwayat": {
            "GERD": 0.9,
            "Gastritis": 0.4,
            "Dispepsia": 0.5,
            "Tukak Lambung": 0.3,
            "Gastroenteritis": 0.2,
            "Lainnya": 0.0,
            "Tidak": 0.0
        },

        "deskripsi":
        """
        GERD adalah kondisi ketika asam lambung naik ke
        kerongkongan sehingga menyebabkan iritasi dan
        sensasi terbakar pada dada.
        """,

        "solusi": [
            "Jangan langsung berbaring setelah makan",
            "Makan dalam porsi sedikit tapi sering",
            "Kurangi makanan berlemak",
            "Kurangi kopi dan minuman bersoda",
            "Tinggikan posisi kepala saat tidur"
        ],
        
        "obat": [
            "Antasida", 
            "Omeprazole*", 
            "Esomeprazole*", 
            "Pantoprazole*"
        ],

        "pantangan": [
            "Kopi",
            "Minuman bersoda",
            "Makanan pedas",
            "Makanan berlemak"
        ]
    },

    "Dispepsia": {

        "kode": "P03",

        "gejala": {

            "G18": 0.8,   # Perut terasa penuh
            "G19": 0.8,   # Tidak nyaman setelah makan
            "G12": 0.6,   # Mual
            "G01": 0.7,   # Nyeri ulu hati
            "G14": 0.5,   # BAB terus-menerus
            "G15": 0.6    # Kotoran lembek dan encer
        },
        
        "onset": {
            "<1 minggu": 0.3,
            "1-4 minggu": 0.6,
            ">1 bulan": 0.8
        },
        
        "riwayat": {
            "Dispepsia": 0.9,
            "Gastritis": 0.5,
            "GERD": 0.4,
            "Tukak Lambung": 0.3,
            "Gastroenteritis": 0.2,
            "Lainnya": 0.0,
            "Tidak": 0.0
        },

        "deskripsi":
        """
        Dispepsia adalah gangguan pencernaan yang
        menimbulkan rasa tidak nyaman pada lambung,
        terutama setelah makan.
        """,

        "solusi": [
            "Makan teratur",
            "Kelola stres",
            "Hindari makan berlebihan",
            "Kurangi makanan berlemak",
            "Batasi makanan pedas"
        ],
        
        "obat": [
            "Antasida", 
            "Domperidone*", 
            "Omeprazole*"
        ],

        "pantangan": [
            "Makanan pedas",
            "Makanan asam",
            "Kafein",
            "Makanan berlemak"
        ]
    },

    "Tukak Lambung": {

        "kode": "P04",

        "gejala": {

            "G01": 0.9,   # Nyeri ulu hati
            "G02": 0.8,   # Perut terasa terbakar
            "G12": 0.7,   # Mual
            "G10": 0.9,   # Muntah darah
            "G13": 0.9,   # BAB hitam
            "G23": 0.8,   # Berat badan menurun
            "G22": 0.6    # Nafsu makan berkurang
        },
        
        "onset": {
            "<1 minggu": 0.3,
            "1-4 minggu": 0.6,
            ">1 bulan": 0.9
        },
        
        "riwayat": {
            "Tukak Lambung": 0.9,
            "Gastritis": 0.5,
            "GERD": 0.4,
            "Dispepsia": 0.5,
            "Gastroenteritis": 0.2,
            "Lainnya": 0.0,
            "Tidak": 0.0
        },

        "deskripsi":
        """
        Tukak lambung merupakan luka pada lapisan
        lambung yang dapat menyebabkan perdarahan
        dan nyeri yang cukup berat.
        """,

        "solusi": [
            "Segera konsultasi ke dokter",
            "Konsumsi makanan yang mudah dicerna",
            "Hindari makanan pedas dan asam",
            "Hindari penggunaan obat sembarangan"
            "Ikuti terapi sesuai anjuran dokter"
        ],
        
        "obat": [
            "Antasida",
            "Sukralfat*", 
            "Omeprazole*", 
            "Lansoprazole*"
        ],

        "pantangan": [
            "Makanan pedas",
            "Makanan asam",
            "Kopi",
            "Rokok"
        ]
    },

    "Gastroenteritis": {

        "kode": "P05",

        "gejala": {

            "G12": 0.7,   # Mual
            "G11": 0.8,   # Muntah
            "G14": 0.9,   # BAB terus-menerus
            "G15": 0.9,   # Kotoran lembek dan encer
            "G16": 0.7,   # Nyeri perut
            "G24": 0.7,   # Demam
            "G26": 0.7,   # Tubuh lemas
            "G27": 0.8    # Dehidrasi
        },
        
        "onset": {
            "<1 minggu": 0.7,
            "1-4 minggu": 0.5,
            ">1 bulan": 0.2
        },
        
        "riwayat": {
            "Gastroenteritis": 0.9,
            "Gastritis": 0.3,
            "GERD": 0.2,
            "Dispepsia": 0.2,
            "Tukak Lambung": 0.1,
            "Lainnya": 0.0,
            "Tidak": 0.0
        },

        "deskripsi":
        """
        Gastroenteritis adalah infeksi pada lambung
        dan usus yang menyebabkan diare, muntah,
        serta kehilangan cairan tubuh.
        """,

        "solusi": [
            "Perbanyak minum air",
            "Konsumsi oralit",
            "Istirahat cukup",
            "Konsumsi makanan yang mudah dicerna"
        ],
        
        "obat": [
            "Oralit", 
            "Zinc", 
            "Paracetamol (jika demam)"
        ],

        "pantangan": [
            "Makanan pedas",
            "Makanan berminyak",
            "Susu berlebihan",
            "Minuman bersoda"
        ]
    }

}