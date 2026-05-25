RULES = {

    "Gastritis (Maag)": {

        "kode": "P01",

        "gejala": {

            "G01": 0.8,
            "G02": 0.6,
            "G03": 0.6,
            "G04": 0.5,
            "G06": 0.5,
            "G07": 0.4,
            "G08": 0.5
        },

        "deskripsi":
        """
        Gastritis (maag) adalah
        peradangan pada dinding
        lambung akibat pola makan
        tidak teratur, stres,
        atau iritasi lambung.
        """,

        "solusi": [
            "Makan teratur",
            "Kurangi makanan pedas",
            "Hindari telat makan",
            "Kurangi kopi"
        ],

        "pantangan": [
            "Pedas",
            "Asam",
            "Kopi",
            "Makanan instan"
        ]
    },


    "GERD": {

        "kode": "P02",

        "gejala": {

            "G05": 0.8,
            "G13": 0.7,
            "G02": 0.5,
            "G06": 0.5,
            "G14": 0.7
        },

        "deskripsi":
        """
        GERD terjadi ketika
        asam lambung naik
        ke kerongkongan dan
        menyebabkan iritasi.
        """,

        "solusi": [
            "Jangan langsung tidur",
            "Makan porsi kecil",
            "Kurangi kopi",
            "Hindari makanan pedas"
        ],

        "pantangan": [
            "Kopi",
            "Pedas",
            "Gorengan",
            "Soda"
        ]
    },


    "Dispepsia": {

        "kode": "P03",

        "gejala": {

            "G04": 0.7,
            "G08": 0.6,
            "G02": 0.5,
            "G01": 0.7,
            "G06": 0.5
        },

        "deskripsi":
        """
        Dispepsia adalah
        gangguan pencernaan
        yang menyebabkan
        rasa tidak nyaman
        pada lambung.
        """,

        "solusi": [
            "Makan teratur",
            "Kelola stres",
            "Kurangi makanan pedas"
        ],

        "pantangan": [
            "Pedas",
            "Asam",
            "Kafein"
        ]
    },


    "Tukak Lambung": {

        "kode": "P04",

        "gejala": {

            "G01": 0.9,
            "G02": 0.7,
            "G11": 0.9,
            "G12": 0.8,
            "G07": 0.5
        },

        "deskripsi":
        """
        Tukak lambung adalah
        luka pada lapisan
        lambung akibat iritasi
        atau infeksi tertentu.
        """,

        "solusi": [
            "Segera konsultasi dokter",
            "Konsumsi makanan lunak",
            "Hindari makanan pedas"
        ],

        "pantangan": [
            "Pedas",
            "Asam",
            "Kopi",
            "Rokok"
        ]
    },


    "Gastroenteritis": {

        "kode": "P05",

        "gejala": {

            "G02": 0.6,
            "G03": 0.8,
            "G09": 0.9,
            "G10": 0.7
        },

        "deskripsi":
        """
        Gastroenteritis adalah
        infeksi lambung dan
        usus yang menyebabkan
        muntah serta diare.
        """,

        "solusi": [
            "Perbanyak cairan",
            "Istirahat cukup",
            "Makan makanan lunak"
        ],

        "pantangan": [
            "Makanan berminyak",
            "Pedas",
            "Susu berlebih"
        ]
    }
}