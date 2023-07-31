from parts import CPU, CPUColler, Motherboard, Memory, Storage, VideoCard, Case, PowerSupply


cpus_data = [
    CPU("Intel", "Core i9-11900k", 399, 8, 16, 3.5, 5.3),
    CPU("Amd", "Ryzen 9 5950x", 299, 16, 32, 3.4, 4.9),
    CPU("Intel", "Core i7-11700k", 239, 8, 16, 3.6, 5.0),
    CPU("Amd", "Ryzen 7 5800x", 200, 8, 16, 3.8, 4.7),
    CPU("Intel", "Core i5-11600k", 209, 6, 12, 3.9, 4.9),
    CPU("Amd", "Ryzen 7 7800X3d", 441, 8, 16, 4.2, 5),
    CPU("Intel", "Core i9-13900k", 409.99, 24, 48, 3, 5.8),
    CPU("Amd", "Ryzen 5 7600x", 199.99, 6, 12, 4.7, 5.3),
    CPU("Intel", "Core i5-13600k", 312.99, 14, 28, 3.5, 5.1),
    CPU("Amd", "Ryzen 7 7700x", 349, 8, 16, 4.5, 5.4),
]

cpu_collers_data = [
    CPUColler("Thermaltake", "A1964", 32.95, 5500, 36),
    CPUColler("Titan", "TTC-NK54TZ", 42.99, 3500, 30.6),
    CPUColler("Amd", "Wraith Prism", 72.83, 2800, 42),
    CPUColler("Cooler Master", "Hyper T2", 35.99, 2800, 35),
    CPUColler("Thermaltake", "CL-P0187", 41.99, 4800, 36),
    CPUColler("Deepcool", "LT720", 139.99, 2250, 32.9),
    CPUColler("NZXT", "Kraken X73", 159.99, 2000, 36),
    CPUColler("Deepcool", "AK620 ZERO DARK", 69.98, 1850, 28),
    CPUColler("Nzxt", "Kraken 240", 139.98, 1800, 30.6),
    CPUColler("Deepcool", "AK620", 63.99, 1850, 28),
]

motherboards_data = [
    Motherboard("Msi", "MAG B550 TOMAHAWK", 169.99, "AM4", "ATX", 128),
    Motherboard("Msi", "B550-A PRO", 139.66, "AM4", "ATX", 128),
    Motherboard("Msi", "B550M PRO-VDH WIFI", 119.99, "AM4", "Micro ATX", 128),
    Motherboard("Gigabyte", "Z790 AORUS ELITE AX",
                249.99, "LGA1700", "ATX", 128),
    Motherboard("Asus", "Prime B450M-A II", 79.98, "AM4", "Micro ATX", 128),
    Motherboard("Gigabyte", "B650 AORUS ELITE AX", 219, "AM5", "ATX", 128),
    Motherboard("Msi", "MAG B660 TOMAHAWK WIFI",
                189.99, "LGA1700", "ATX", 128),
    Motherboard("Asus", "ROG STRIX B550-A GAMING", 169.99, "AM4", "ATX", 128),
    Motherboard("Msi", "MAG B650 TOMAHAWK WIFI", 219.99, "AM5", "ATX", 128),
    Motherboard("Msi", "MAG Z790 TOMAHAWK WIFI",
                259.99, "LGA1700", "ATX",	192),

]

memories_data = [
    Memory("Corsair", "Vengeance LPX", 39.99, 16, "DDR4", 3200),
    Memory("Corsair", "Vengeance RGB Pro", 99.99, 32, "DDR4", 3600),
    Memory("Corsair", "Vengeance LPX", 69.98, 32, "DDR4", 3600),
    Memory("Corsair", "Vengeance", 97.99, 32, "DDR5", 5600),
    Memory("G.Skill", "Trident Z5 RGB", 104.99, 32, "DDR5", 6000),
    Memory("Corsair", "Vengeance RGB Pro", 54.74, 16, "DDR4", 3200),
    Memory("G.Skill", "Trident Z5 RGB", 224.99, 64, "DDR5", 6400),
    Memory("Corsair", "Vengeance", 102.99, 32, "DDR5", 6000),
    Memory("Corsair", "Vengeance RGB", 107.99, 32, "DDR5", 6000),
    Memory("Silicon", "Power GAMING", 29.97, 16, "DDR4", 3200),

]

storages_data = [
    Storage("Samsung", "980 Pro", 119.99, "2TB", "SSD", "M.2 PCIe 4.0 X4"),
    Storage("Samsung", "970 Evo Plus", 49.99, "1TB", "SSD", "M.2 PCIe 3.0 X4"),
    Storage("Samsung", "980 Pro", 69.98, "1TB", "SSD", "M.2 PCIe 4.0 X4"),
    Storage("Kingston", "NV2", 42.70, "1TB", "SSD", "M.2 PCIe 4.0 X4"),
    Storage("Seagate", "Barracuda Compute", 55.49,
            "2TB", "7200 RPM", " SATA 6.0 Gb/s"),
    Storage("Samsung", "990 Pro", 149.99, "2TB", "SSD", "M.2 PCIe 4.0 X4"),
    Storage("Samsung", "970 Evo Plus", 97.13, "2TB", "SSD", "M.2 PCIe 3.0 X4"),
    Storage("Crucial", "P3", 39.99,	"1TB", "SSD", "M.2 PCIe 3.0 X4"),
    Storage("Western Digital", "Black SN850X",
            99.99, "2TB", "SSD", "M.2 PCIe 4.0 X4"),
    Storage("Western Digital", "Black SN770",
            45.99, "1TB", "SSD", "M.2 PCIe 4.0 X4"),

]

video_cards_data = [
    VideoCard("Xfx", "Speedster MERC 310 Black Edition",
              979.99, "Radeon RX 7900 XTX", 24, 2300, 2615),
    VideoCard("Gigabyte", "WINDFORCE OC", 599.99,
              "GeForce RTX 4070", 12, 1920, 2490),
    VideoCard("Asus", "ROG STRIX GAMING OC", 1951.79,
              "GeForce RTX 4090", 24, 2235, 2640),
    VideoCard("ASRock", "Challenger D", 179.99,
              "Radeon RX 6600", 8, 1626, 1920),
    VideoCard("Xfx", "Speedster MERC 319", 629.99,
              "Radeon RX 6950 XT", 16, 2009, 2368),
    VideoCard("Xfx", "Speedster MERC 319 CORE", 529.99,
              "Radeon RX 6800 XT", 16, 1825, 2250),
    VideoCard("Asus", "TUF GAMING", 799.99,
              "GeForce RTX 4070 Ti", 12, 2310, 2640),
    VideoCard("Msi", "Ventus OC", 284.99, "GeForce RTX 3060", 12, 1320, 1807),
    VideoCard("Gigabyte", "EAGLE", 234.99, "Radeon RX 6600", 8, 1626, 2491),
    VideoCard("Msi", "VENTUS X3 OC", 609, "GeForce RTX 4070", 12, 1920, 2491),

]

cases_data = [
    Case("Corsair", "4000D Airflow", 89.99,
         "ATX Mid Tower", "Black", "Tinted Tempered Glass"),
    Case("Nzxt", "H5 Flow", 94.99, "ATX Mid Tower", "Black", "Tempered Glass"),
    Case("Deepcool", "CC560", 67.98, "ATX Mid Tower", "Black", "Tempered Glass"),
    Case("Lian Li", "O11 Dynamic EVO", 152.99,
         "ATX Mid Tower", "White", "Tempered Glass"),
    Case("Nzxt", "H9 Flow", 154.99, "ATX Mid Tower",
         "Gray", "Tinted Tempered Glass"),
    Case("Corsair", "iCUE 4000X RGB", 79.98,
         "ATX Mid Tower", "Black", "Tempered Glass"),
    Case("Fractal Design", "North", 166.98,
         "ATX Mid Tower", "White", "Tempered Glass"),
    Case("Thermaltake", "Versa H18", 129.99,
         "MicroATX", "White", "Tempered Glass"),
    Case("Corsair", "4000D Airflow", 69.99,
         "ATX Mid Tower", "Black", "Tinted Tempered Glass"),
    Case("Fractal Design", "Pop Air", 79.99,
         "ATX Mid Tower", " Black", "Tempered Glass"),

]

power_supplies_data = [
    PowerSupply("Corsair", "RM750e", 99.99, "ATX", "80+ Gold", 750, "Full"),
    PowerSupply("Corsair", "RM850x", 129.99, "ATX", "80+ Gold", 850, "Full"),
    PowerSupply("Corsair", " RM1000x", 169.99,
                "ATX", "80+ Gold", 1000, "Full"),
    PowerSupply("Thermaltake", "Toughpower GX2",
                67.98, "ATX", "80+ Gold", 650, "No"),
    PowerSupply("Corsair", "CX650M", 76.99, "ATX", "80+ Bronze", 650, "Semi"),
    PowerSupply("Corsair", "RM750x", 114, "ATX", "80+ Gold", 750, "Full"),
    PowerSupply("Corsair", "SF750", 89.99, "SFX", "80+ Gold", 750, "No"),
    PowerSupply("Corsair", "RM850", 139.99, "ATX",
                "80+ Platinum", 850, "Full"),
    PowerSupply("Corsair", "RM850e", 119.00, "ATX", " 80+ Gold", 850, "Full"),
    PowerSupply("Corsair", "RM1000e", 163.27, "ATX", "80+ Gold", 1000, "Full"),

]

parts_dict = {
    "cpu": cpus_data,
    "cpu_coller": cpu_collers_data,
    "motherboard": motherboards_data,
    "ram": memories_data,
    "storage": storages_data,
    "gpu": video_cards_data,
    "case": cases_data,
    "psu": power_supplies_data,

}
