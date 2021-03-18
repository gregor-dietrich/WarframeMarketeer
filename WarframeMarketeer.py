import datetime

from Cache import Cache
from Drop import Drop
from Relic import Relic

relic_dict = {
    "Lith": [
        "A1",
        "A2",
        "A3",
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
        "B6",
        "B7",
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "D1",
        "D2",
        "D3",
        "F1",
        "F2",
        "G1",
        "G2",
        "G3",
        "H1",
        "H2",
        "I1",
        "K1",
        "K2",
        "K3",
        "K4",
        "K5",
        "L1",
        "L2",
        "M1",
        "M2",
        "M3",
        "M4",
        "M5",
        "M6",
        "M7",
        "N1",
        "N2",
        "N3",
        "N4",
        "N5",
        "N6",
        "O1",
        "O2",
        "P1",
        "P2",
        "P3",
        "P4",
        "P5",
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
        "T1",
        "T2",
        "T3",
        "T4",
        "T5",
        "V1",
        "V2",
        "V3",
        "V4",
        "V5",
        "V6",
        "V7",
        "V8",
        "W1",
        "W2",
        "Z1",
        "Z2"
    ],
    "Meso": [
        "A1",
        "A2",
        "B1",
        "B2",
        "B3",
        "B4",
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "D1",
        "D2",
        "D3",
        "D4",
        "D5",
        "D6",
        "E1",
        "E2",
        "E3",
        "E4",
        "E5",
        "F1",
        "F2",
        "F3",
        "G1",
        "G2",
        "H1",
        "I1",
        "K1",
        "K2",
        "K3",
        "L1",
        "M1",
        "M2",
        "M3",
        "N1",
        "N2",
        "N3",
        "N4",
        "N5",
        "N6",
        "N7",
        "N8",
        "N9",
        "N10",
        "O1",
        "O2",
        "O3",
        "O4",
        "P1",
        "P2",
        "P3",
        "R1",
        "R2",
        "R3",
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "T1",
        "T2",
        "T3",
        "T4",
        "V1",
        "V2",
        "V3",
        "V4",
        "V5",
        "V6",
        "W1",
        "Z1",
        "Z2",
        "Z3"
    ],
    "Neo": [
        "A1",
        "A2",
        "A3",
        "A4",
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
        "B6",
        "B7",
        "C1",
        "D1",
        "D2",
        "E1",
        "E2",
        "F1",
        "G1",
        "G2",
        "G3",
        "H1",
        "H2",
        "I1",
        "I2",
        "K1",
        "K2",
        "L1",
        "M1",
        "M2",
        "M3",
        "N1",
        "N2",
        "N3",
        "N4",
        "N5",
        "N6",
        "N7",
        "N8",
        "N9",
        "N10",
        "N11",
        "N12",
        "N13",
        "O1",
        "P1",
        "P2",
        "R1",
        "R2",
        "R3",
        "R4",
        "S1",
        "S2",
        "S3",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
        "S11",
        "S12",
        "S13",
        "S14",
        "T1",
        "T2",
        "T3",
        "V1",
        "V2",
        "V3",
        "V4",
        "V5",
        "V6",
        "V7",
        "V8",
        "Z1",
        "Z2",
        "Z3",
        "Z4",
        "Z5",
        "Z6",
        "Z7",
    ],
    "Axi": [
        "A1",
        "A2",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
        "A9",
        "A10",
        "A11",
        "A12",
        "B1",
        "B2",
        "B3",
        "B4",
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "D1",
        "D2",
        "E1",
        "E2",
        "G1",
        "G2",
        "G3",
        "G4",
        "H1",
        "H2",
        "H3",
        "H4",
        "H5",
        "K1",
        "K2",
        "K3",
        "K4",
        "K5",
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "M1",
        "N1",
        "N2",
        "N3",
        "N4",
        "N5",
        "N6",
        "O1",
        "O2",
        "O3",
        "O4",
        "O5",
        "P1",
        "P2",
        "P3",
        "R1",
        "R2",
        "R3",
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "T1",
        "T2",
        "T3",
        "T4",
        "T5",
        "T6",
        "V1",
        "V2",
        "V3",
        "V4",
        "V5",
        "V6",
        "V7",
        "V8",
        "V9",
        "W1",
        "Z1"
    ],
    "Requiem": [
        "I",
        "II",
        "III",
        "IV"
    ]
}


class WarframeMarketeer:
    def __init__(self):
        self.cache = Cache()

    def build_cache(self):
        all_relics = []
        for prefix in relic_dict.keys():
            for relic in relic_dict[prefix]:
                all_relics.append(prefix + " " + relic)
        start_time = str(datetime.datetime.now())
        for relic_name in all_relics:
            Relic(self.cache, relic_name)
        print("Start: " + start_time)
        print("End: " + str(datetime.datetime.now()))
        if self.cache.needs_save:
            self.cache.save()

    # Relic Printing
    def print_all_relics(self):
        all_relics = []
        for prefix in relic_dict.keys():
            for relic in relic_dict[prefix]:
                all_relics.append(prefix + " " + relic)
        self.print_list_relics(all_relics)

    def print_list_relics(self, relics):
        drops = {}
        for relic_name in relics:
            relic = Relic(self.cache, relic_name)
            for drop in relic.drops:
                if drop.platinum != "N/A":
                    drops[drop.name] = drop.platinum
                else:
                    drops[drop.name] = 0
        for drop in sorted(drops.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
            print(drop[0] + ": " + str(drop[1]))
        if self.cache.needs_save:
            self.cache.save()

    def print_list_relics_values(self, comparison_dict):
        for prefix in comparison_dict.keys():
            for relic_id in comparison_dict[prefix]:
                relic = Relic(self.cache, prefix + " " + relic_id)
                print(relic.name)
        if self.cache.needs_save:
            self.cache.save()

    def print_prefix_relics(self, prefix):
        prefix_relics = []
        if prefix in relic_dict.keys():
            for relic in relic_dict[prefix]:
                prefix_relics.append(prefix + " " + relic)
            self.print_list_relics(prefix_relics)
        else:
            print("ERROR: invalid prefix")

    def print_relic(self, relic_name):
        relic = Relic(self.cache, relic_name)
        if relic.vaulted == "Baro":
            is_vaulted = " (Baro Ki'Teer exclusive)"
        else:
            is_vaulted = " (Vaulted: Yes)" if relic.vaulted else " (Vaulted: No)"
        print(relic.name + is_vaulted)
        total = 0
        for drop in relic.drops:
            print(drop.name + ": " + str(drop.platinum) + " (" + str(drop.chance) + "%) | "
                  + str(drop.ducats) + " ducats")
            try:
                total += drop.platinum * drop.chance
            except TypeError:
                total = -1
                break
        if total == -1:
            print("Average Drop Value: N/A")
        else:
            print("Average Drop Value: " + str(round(total / 100, 1)))
        print("Relic Market Price: " + str(relic.platinum))
        if self.cache.needs_save:
            self.cache.save()

    # Drop Printing
    def print_list_drops(self, drop_names):
        drops = []
        for drop_name in drop_names:
            drops.append(Drop(self.cache, drop_name))
        drops_dict, plat_dict = {}, {}
        for drop in drops:
            drops_dict[drop.name] = drop
            if drop.platinum != "N/A":
                plat_dict[drop.name] = drop.ducats / drop.platinum
            else:
                plat_dict[drop.name] = 0
        for drop in sorted(plat_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
            print(drop[0] + ": " + str(drops_dict[drop[0]].platinum) + " | " + str(drops_dict[drop[0]].ducats) +
                  " ducats (" + str(round(drops_dict[drop[0]].ducats / drops_dict[drop[0]].platinum, 1)) + " duc/plat)")
        if self.cache.needs_save:
            self.cache.save()

    def print_drop(self, drop_name):
        drop = Drop(self.cache, drop_name)
        print(drop.name + ": " + str(drop.platinum) + " | " + str(drop.ducats) + " ducats")
        if self.cache.needs_save:
            self.cache.save()
