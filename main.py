from WarframeMarketeer import *


if __name__ == "__main__":
    app = WarframeMarketeer()

    # Build the cache!
    # app.build_cache()

    # Compare all relics
    # app.print_all_relics()

    # Compare all relics of a prefix
    # app.print_prefix_relics("Neo")

    # Show details about a relic
    # app.print_relic("Neo P2")

    # Show details about an item
    # app.print_drop("Pandero Prime Receiver")

    # Compare a squad's relics
    prefix = "Lith"
    ids = "C4, I1"
    relic_list = []
    for i in ids.replace(",", "").split(" "):
        relic_list.append(prefix + " " + i)
    # app.print_list_relics(relic_list)

    # Compare multiple items
    item_list = [
        "Atlas Prime Blueprint",
        "Ivara Prime Blueprint",
        "Ivara Prime Neuroptics",
        "Ivara Prime Systems",
        "Limbo Prime Systems",
        "Mesa Prime Blueprint",
        "Mirage Prime Neuroptics",
        "Pandero Prime Receiver",
        "Titania Prime Blueprint",
        "Wukong Prime Chassis"
    ]
    # app.print_list_drops(item_list)

    # Compare relic values
    relic_dict = {
        "Lith": [
            "A2",
            "A3",
            "B2",
            "B4",
            "B6",
            "B7",
            "B8",
            "C2",
            "C4",
            "D3",
            "D4",
            "G1",
            "G3",
            "H1",
            "H2",
            "I1",
            "K1",
            "K2",
            "K5",
            "L1",
            "M3",
            "M4",
            "M7",
            "N2",
            "N3",
            "N5",
            "N6",
            "O1",
            "O2",
            "P2",
            "P4",
            "P5",
            "S1",
            "S4",
            "S5",
            "T1",
            "T4",
            "T5",
            "V1",
            "V2",
            "V3",
            "V4",
            "W1"
        ],
        "Meso": [
            "A1",
            "B1",
            "C3",
            "C6",
            "D1",
            "D3",
            "D6",
            "E2",
            "E4",
            "E5",
            "F1",
            "G1",
            "G2",
            "H1",
            "I1",
            "K1",
            "K2",
            "K3",
            "M3",
            "N1",
            "N2",
            "N3",
            "N4",
            "N5",
            "N10",
            "O1",
            "O2",
            "P1",
            "P2",
            "P4",
            "R1",
            "S2",
            "S3",
            "S4",
            "S6",
            "S8",
            "T1",
            "T3",
            "T4",
            "V1",
            "V2",
            "V4",
            "V5",
            "Z2",
            "Z3"
        ],
        "Neo": [
            "A1",
            "A2",
            "B1",
            "B2",
            "B6",
            "B7",
            "C1",
            "D2",
            "G1",
            "H1",
            "I2",
            "M1",
            "M2",
            "N4",
            "N5",
            "N6",
            "N7",
            "N8",
            "N10",
            "N13",
            "N14",
            "P2",
            "S7",
            "S8",
            "S9",
            "S11",
            "S14",
            "T1",
            "T2",
            "V2",
            "V3",
            "V4",
            "V5",
            "Z2",
            "Z6",
            "Z7"
        ],
        "Axi": [
            "A1",
            "A3",
            "A11",
            "A12",
            "A13",
            "B2",
            "B3",
            "C1",
            "C2",
            "C6",
            "E2",
            "G1",
            "H1",
            "H2",
            "H4",
            "H5",
			"K5",
            "L3",
            "L5",
            "N1",
            "N2",
            "N4",
            "N5",
            "N6",
            "O1",
            "O5",
            "R1",
            "R2",
            "T2",
            "T4",
            "T6",
            "V5",
            "V6",
            "V7",
            "W2",
            "Z1"
        ],
        "Requiem": []
    }
    app.print_list_relics_values(relic_dict)
