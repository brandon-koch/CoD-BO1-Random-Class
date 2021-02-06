# Call of Duty BO1 Class Randomizer
import random

All_Primary = ["MP5K", "Skorpion", "MAC11", "AK74u", "Uzi", "PM63", "MPL", "Spectre", "Kiparis",
               "M16", "Enfield", "M14", "Famas", "Galil", "AUG", "FN FAL", "AK-47", "Commando", "G11",
               "Olympia", "Stakeout", "SPAS-12", "HS10",
               "HK21", "RPK", "M60", "Stoner63",
               "Dragunov", "WA2000", "L96A1", "PSG1"]

SMGs = ["MP5K", "Skorpion", "MAC11", "AK74u", "Uzi", "PM63", "MPL", "Spectre", "Kiparis"]
ARs = ["M16", "Enfield", "M14", "Famas", "Galil", "AUG", "FN FAL", "AK-47", "Commando", "G11"]
Shotguns = ["Olympia", "Stakeout", "SPAS-12", "HS10"]
LMGs = ["HK21", "RPK", "M60", "Stoner63"] 
Snipers = ["Dragunov", "WA2000", "L96A1", "PSG1"]

MP5K_A = ["None", "Extended Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Suppressor", "Rapid Fire"]
Skorpion_A = ["None", "Extended Mag", "Grip", "Dual Wield", "Suppressor", "Rapid Fire"]
MAC11_A = ["None", "Extended Mag", "Red Dot Sight", "Reflex Sight", "Grip", "Dual Wield", "Suppressor", "Rapid Fire"]
AK74u_A = ["None", "Extended Mag", "Dual Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", 
           "Grip", "Suppressor", "Grenade Launcher", "Rapid Fire"]
Uzi_Spectre_A = ["None", "Extended Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Suppressor", "Rapid Fire"]
PM63_A = ["None", "Extended Mag", "Grip", "Dual Wield", "Rapid Fire"]
MPL_A = ["None", "Dual Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Suppressor", "Rapid Fire"]
Kiparis_A = ["None", "Extended Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Dual Wield", "Suppressor", "Rapid Fire"]

AR_A = ["None", "Extended Mag", "Dual Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", 
        "Masterkey", "Flamethrower", "Infared Scope", "Suppressor", "Grenade Launcher"]
M14_A = ["None", "Extended Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip",
         "Masterkey", "Flamethrower", "Infared Scope", "Suppressor", "Grenade Launcher"]
G11_A = ["None", "Low Power Scope", "Variable Zoom"]

Stakeout_A = ["None", "Grip"]
SPAS_12_A = ["None", "Suppressor"]
HS10_A = ["None", "Dual Wield"]

HK21_Stoner63_A = ["None", "Extended Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Infared Scope"]
RPK_A = ["None", "Extended Mag", "Dual Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Infared Scope"]
M60_A = ["None", "Extended Mag", "ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Infared Scope"]

Snipers_A = ["None", "Extended Mag", "ACOG Sight", "Infared Scope", "Suppressor", "Variable Zoom"]

Camos = ["None", "Dusty", "Ice", "Red", "Olive", "Nevada", "Sahara", "ERDL", "Tiger",
         "Berlin", "Warsaw", "Siberia", "Yukon", "Woodland", "Flora", "Gold"]

All_Secondary = ["ASP", "M1911", "Makarov", "Python", "CZ75",
                 "M72 LAW", "RPG", "Strela-3", "China Lake",
                 "Ballistic Knife", "Crossbow"]

Pistols = ["ASP", "M1911", "Makarov", "Python", "CZ75"]
Launchers = ["M72 LAW", "RPG", "Strela-3", "China Lake"]
Specials = ["Ballistic Knife", "Crossbow"]        

ASP_A = ["None", "Dual Wield"]
M1911_Makarov_A = ["None", "Upgraded Iron Sights", "Extended Mag", "Dual Wield", "Suppressor"]
Python_A = ["None", "ACOG Sight", "Snub Nose", "Speed Reloader", "Dual Wield"]
CZ75_A = ["None", "Upgraded Iron Sights", "Extended Mag", "Dual Wield", "Suppressor", "Full Auto Upgrade"]

Lethal = ["Frag", "Semtex", "Tomahawk"]
Tactical = ["Willy Pete", "Nova Gas", "Flashbang", "Concussion", "Decoy"]
Equipment = ["Camera Spike", "C4", "Tactical Insertion", "Jammer", "Motion Sensor", "Claymore"]

Perk1 = ["Lightweight", "Scavenger", "Ghost", "Flak Jacket", "Hardline"]
Perk2 = ["Hardened", "Scout", "Steady Aim", "Sleight of Hand", "Warlord"]
Perk3 = ["Tactical Mask", "Marathon", "Ninja", "Second Chance", "Hacker"]

Killstreaks = {"Spy Plane": 3, "RC-XD": 3, "Counter-Spy Plane": 4, "SAM Turret": 4, "Care Package": 5, "Napalm Strike": 5, 
               "Sentry Gun": 6, "Mortar Team": 6, "Attack Helicopter": 7, "Valkyrie Rockets": 7, "Blackbird": 8, 
               "Rolling Thunder": 8, "Chopper Gunner": 9, "Attack Dogs": 11, "Gunship": 11}

def generate():
    primary = random.choice(All_Primary)
    print(f"\nPrimary: {primary}")
    if primary == "G11" or primary in Shotguns:
        Perk2.remove("Warlord")
    P2 = random.choice(Perk2)
    if P2 == "Warlord":
        if primary in SMGs:

            if primary == "MP5K":
                MP5K_A.remove("None")
                A1 = random.choice(MP5K_A)
                if A1 == "Extended Mag" or A1 == "Rapid Fire":
                    A2 = random.choice(MP5K_A[2:6])
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight":
                    MP5K_Sight = ["Extended Mag", "Suppressor", "Rapid Fire"]
                    A2 = random.choice(MP5K_Sight)
                elif A1 == "Suppressor":
                    MP5K_A.remove("Suppressor")
                    A2 = random.choice(MP5K_A[1:])

            elif primary == "Skorpion":
                Skorpion_A.remove("None")
                Skorpion_A.remove("Dual Wield")
                A1 = random.choice(Skorpion_A)
                if A1 == "Extended Mag" or A1 == "Rapid Fire":
                    Skorpion_Mag_Rap = ["Grip", "Suppressor"]
                    A2 = random.choice(Skorpion_Mag_Rap)
                elif A1 == "Grip":
                    Skorpion_A.remove("Grip")
                    A2 = random.choice(Skorpion_A)
                elif A1 == "Suppressor":
                    Skorpion_A.remove("Suppressor")
                    A2 = random.choice(Skorpion_A)
            
            elif primary == "MAC11":
                MAC11_A.remove("None")
                MAC11_A.remove("Dual Wield")
                A1 = random.choice(MAC11_A)
                if A1 == "Extended Mag" or A1 == "Rapid Fire":
                    MAC11_Mag_Rap = ["Red Dot Sight", "Reflex Sight", "Grip", "Suppressor"]
                    A2 = random.choice(MAC11_Mag_Rap)
                elif A1 == "Red Dot Sight" or A1 == "Reflex Sight":
                    MAC11_Sight = ["Extended Mag", "Grip", "Suppressor", "Rapid Fire"]
                    A2 = random.choice(MAC11_Sight)
                elif A1 == "Grip":
                    MAC11_A.remove("Grip")
                    A2 = random.choice(MAC11_A)
                elif A1 == "Suppressor":
                    MAC11_A.remove("Suppressor")
                    A2 = random.choice(MAC11_A)
            
            elif primary == "AK74u":
                AK74u_A.remove("None")
                AK74u_A.remove("Grenade Launcher")
                A1 = random.choice(AK74u_A)
                if A1 == "Extended Mag" or A1 == "Dual Mag" or A1 == "Rapid Fire":
                    AK74u_EDR = ["ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Suppressor"]
                    A2 = random.choice(AK74u_EDR)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight":
                    AK74u_Sight = ["Extended Mag", "Dual Mag", "Grip", "Suppressor", "Rapid Fire"]
                    A2 = random.choice(AK74u_Sight)
                elif A1 == "Grip":
                    AK74u_A.remove("Grip")
                    A2 = random.choice(AK74u_A)
                elif A1 == "Suppressor":
                    AK74u_A.remove("Suppressor")
                    A2 = random.choice(AK74u_A)
            
            elif primary == "Uzi" or primary == "Spectre":
                Uzi_Spectre_A.remove("None")
                A1 = random.choice(Uzi_Spectre_A)
                if A1 == "Extended Mag":
                    Uzi_Spectre_A.remove("Extended Mag")
                    A2 = random.choice(Uzi_Spectre_A)
                elif A1 == "Rapid Fire":
                    Uzi_Spectre_A.remove("Rapid Fire")
                    A2 = random.choice(Uzi_Spectre_A)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight":
                    Uzi_Spectre_Sight = ["Extended Mag", "Grip", "Suppressor", "Rapid Fire"]
                    A2 = random.choice(Uzi_Spectre_Sight)
                elif A1 == "Grip":
                    Uzi_Spectre_A.remove("Grip")
                    A2 = random.choice(Uzi_Spectre_A)
                elif A1 == "Suppressor":
                    Uzi_Spectre_A.remove("Suppressor")
                    A2 = random.choice(Uzi_Spectre_A)    

            elif primary == "PM63":
                PM63_A.remove("None")
                PM63_A.remove("Dual Wield")
                A1 = random.choice(PM63_A)
                if A1 == "Extended Mag" or A1 == "Rapid Fire":
                    A2 = "Grip"
                elif A1 == "Grip":
                    PM63_Grip = ["Extended Mag", "Rapid Fire"]
                    A2 = random.choice(PM63_Grip)

            elif primary == "MPL":
                MPL_A.remove("None")
                A1 = random.choice(MPL_A)
                if A1 == "Dual Mag" or A1 == "Rapid Fire":
                    MPL_DR = ["ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Suppressor"]
                    A2 = random.choice(MPL_DR)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight":
                    MPL_Sight = ["Dual Mag", "Grip", "Suppressor", "Rapid Fire"]
                    A2 = random.choice(MPL_Sight)
                elif A1 == "Grip":
                    MPL_A.remove("Grip")
                    A2 = random.choice(MPL_A)
                elif A1 == "Suppressor":
                    MPL_A.remove("Suppressor")
                    A2 = random.choice(MPL_A)

            elif primary == "Kiparis":
                Kiparis_A.remove("None")
                Kiparis_A.remove("Dual Wield")
                A1 = random.choice(Kiparis_A)
                if A1 == "Extended Mag" or A1 == "Rapid Fire":
                    Kiparis_ER = ["ACOG Sight", "Red Dot Sight", "Reflex Sight", "Grip", "Suppressor"]
                    A2 = random.choice(Kiparis_ER)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight":
                    Kiparis_Sight = ["Extended Mag", "Grip", "Suppressor", "Rapid Fire"]
                    A2 = random.choice(Kiparis_Sight)
                elif A1 == "Grip":
                    Kiparis_A.remove("Grip")
                    A2 = random.choice(Kiparis_A)
                elif A1 == "Suppressor":
                    Kiparis_A.remove("Suppressor")
                    A2 = random.choice(Kiparis_A)        
            
        elif primary in ARs:
            if primary == "M14":
                M14_A.remove("None")
                M14_A.remove("Masterkey")
                M14_A.remove("Flamethrower")
                M14_A.remove("Grenade Launcher")
                A1 = random.choice(M14_A)
                if A1 == "Extended Mag":
                    M14_A.remove("Extended Mag")
                    A2 = random.choice(M14_A)
                elif A1 == "Grip":
                    M14_A.remove("Grip")
                    A2 = random.choice(M14_A)
                elif A1 == "Suppressor":
                    M14_A.remove("Suppressor")
                    A2 = random.choice(M14_A)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight" or A1 == "Infared Scope":
                    M14_Sight = ["Extended Mag", "Grip", "Suppressor"]
                    A2 = random.choice(M14_Sight)
            
            else:
                AR_A.remove("None")
                AR_A.remove("Masterkey")
                AR_A.remove("Flamethrower")
                AR_A.remove("Grenade Launcher")
                A1 = random.choice(AR_A)
                if A1 == "Extended Mag" or A1 == "Dual Mag":
                    AR_ED = ["ACOG Sight", "Red Dot Sight", "Reflex Sight", "Infared Scope", "Suppressor"]
                    A2 = random.choice(AR_ED)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight" or A1 == "Infared Scope":
                    AR_Sight = ["Extended Mag", "Dual Mag", "Suppressor"]
                    A2 = random.choice(AR_Sight)
                
        elif primary in LMGs:
            if primary == "HK21" or "Stoner63":
                HK21_Stoner63_A.remove("None")
                A1 = random.choice(HK21_Stoner63_A)
                if A1 == "Extended Mag":
                    HK21_Stoner63_A.remove("Extended Mag")
                    A2 = random.choice(HK21_Stoner63_A)
                else:
                    A2 = "Extended Mag"
            
            elif primary == "RPK":
                RPK_A.remove("None")
                A1 = random.choice(RPK_A)
                if A1 == "Extended Mag" or A1 == "Dual Mag":
                    RPK_ED = ["ACOG Sight", "Red Dot Sight", "Reflex Sight", "Infared Scope"]
                    A2 = random.choice(RPK_ED)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight" or A1 == "Infared Scope":
                    RPK_Sight = ["Extended Mag", "Dual Mag"]
                    A2 = random.choice(RPK_Sight)
                
            elif primary == "M60":
                M60_A.remove("None")
                A1 = random.choice(M60_A)
                if A1 == "Extended Mag":
                    M60_A.remove("Extended Mag")
                    A2 = random.choice(M60_A)
                elif A1 == "Grip":
                    M60_A.remove("Grip")
                    A2 = random.choice(M60_A)
                elif A1 == "ACOG Sight" or A1 == "Red Dot Sight" or A1 == "Reflex Sight" or A1 == "Infared Scope":
                    M60_Sight = ["Extended Mag", "Grip"]
                    A2 = random.choice(M60_Sight)
            
        elif primary in Snipers:
            Snipers_A.remove("None")
            A1 = random.choice(Snipers_A)
            if A1 == "Extended Mag":
                Snipers_A.remove("Extended Mag")
                A2 = random.choice(Snipers_A)
            elif A1 == "Suppressor":
                Snipers_A.remove("Suppressor")
                A2 = random.choice(Snipers_A)
            elif A1 == "ACOG Sight" or A1 == "Infared Scope" or A1 == "Variable Zoom":
                Snipers_Sight = ["Extended Mag", "Suppressor"]
                A2 = random.choice(Snipers_Sight)
        print("Attachments: " + str(A1) + ", " + str(A2))

    else:
        A2 = "None"
        if primary in SMGs:
            if primary == "MP5K":
                A1 = random.choice(MP5K_A)
            elif primary == "Skorpion":
                A1 = random.choice(Skorpion_A)
            elif primary == "MAC11":
                A1 = random.choice(MAC11_A)
            elif primary == "AK74u":
                A1 = random.choice(AK74u_A)
            elif primary == "Uzi" or primary == "Spectre":
                A1 = random.choice(Uzi_Spectre_A)
            elif primary == "PM63":
                A1 = random.choice(PM63_A)
            elif primary == "MPL":
                A1 = random.choice(MPL_A)
            elif primary == "Kiparis":
                A1 = random.choice(Kiparis_A)

        elif primary in ARs:
            if primary == "M14":
                A1 = random.choice(M14_A)
            elif primary == "G11":
                A1 = random.choice(G11_A)
            else:
                A1 = random.choice(AR_A)
        
        elif primary in LMGs:
            if primary == "HK21" or "Stoner63":
                A1 = random.choice(HK21_Stoner63_A)
            elif primary == "RPK":
                A1 = random.choice(RPK_A)
            elif primary == "M60":
                A1 = random.choice(M60_A)

        elif primary in Shotguns:
            if primary == "Olympia":
                A1 = "None"
            elif primary == "Stakeout":
                A1 = random.choice(Stakeout_A)
            elif primary == "SPAS-12":
                A1 = random.choice(SPAS_12_A)
            elif primary == "HS10":
                A1 = random.choice(HS10_A)
        
        elif primary in Snipers:
            A1 = random.choice(Snipers_A)
    if A1 == "None":
        if primary != "Olympia":
            print("Attachments: None")
    if A1 != "None":
        if P2 != "Warlord":
            print(f"Attachments: {A1}")

    C = random.choice(Camos)
    print(f"Camo: {C}")

    secondary = random.choice(All_Secondary)
    print(f"\nSecondary: {secondary}")
    if secondary in Pistols:
        if secondary == "ASP":
            S_A = random.choice(ASP_A)
        elif secondary == "M1911" or secondary == "Makarov":
            S_A = random.choice(M1911_Makarov_A)
        elif secondary == "Python":
            S_A = random.choice(Python_A)
        elif secondary == "CZ75":
            S_A = random.choice(CZ75_A)
        if S_A == "None":
            print("Attachments: None")
        
    else:
        S_A = "None"

    if S_A != "None":
        print(f"Attachment: {S_A}")
    
    L = random.choice(Lethal)
    print("\nLethal: " + str(L))
    T = random.choice(Tactical)
    print("Tactical: " + str(T))
    E = random.choice(Equipment)
    print("Equipment: " + str(E))

    P1 = random.choice(Perk1)
    print("\nPerk 1: " + str(P1))
    print(f"Perk 2: {P2}")
    P3 = random.choice(Perk3)
    print(f"Perk 3: {P3}")

    K_List = list(Killstreaks)
    K1 = random.choice(K_List)
    print("\nKillstreaks:")
    if K1 == "Spy Plane" or K1 == "RC-XD":
        K_List.remove("Spy Plane")
        K_List.remove("RC-XD")
    elif K1 == "Counter-Spy Plane" or K1 == "SAM Turret":
        K_List.remove("Counter-Spy Plane")
        K_List.remove("SAM Turret")
    elif K1 == "Care Package" or K1 == "Napalm Strike":
        K_List.remove("Care Package")
        K_List.remove("Napalm Strike")
    elif K1 == "Sentry Gun" or K1 == "Mortar Team":
        K_List.remove("Sentry Gun")
        K_List.remove("Mortar Team")
    elif K1 == "Attack Helicopter" or K1 == "Valkyrie Rockets":
        K_List.remove("Attack Helicopter")
        K_List.remove("Valkyrie Rockets")
    elif K1 == "Blackbird" or K1 == "Rolling Thunder":
        K_List.remove("Blackbird")
        K_List.remove("Rolling Thunder")
    elif K1 == "Chopper Gunner":
        K_List.remove("Chopper Gunner")
    elif K1 == "Attack Dogs" or K1 == "Gunship":
        K_List.remove("Attack Dogs")
        K_List.remove("Gunship")

    K2 = random.choice(K_List)
    if K2 == "Spy Plane" or K2 == "RC-XD":
        K_List.remove("Spy Plane")
        K_List.remove("RC-XD")
    elif K2 == "Counter-Spy Plane" or K2 == "SAM Turret":
        K_List.remove("Counter-Spy Plane")
        K_List.remove("SAM Turret")
    elif K2 == "Care Package" or K2 == "Napalm Strike":
        K_List.remove("Care Package")
        K_List.remove("Napalm Strike")
    elif K2 == "Sentry Gun" or K2 == "Mortar Team":
        K_List.remove("Sentry Gun")
        K_List.remove("Mortar Team")
    elif K2 == "Attack Helicopter" or K2 == "Valkyrie Rockets":
        K_List.remove("Attack Helicopter")
        K_List.remove("Valkyrie Rockets")
    elif K2 == "Blackbird" or K2 == "Rolling Thunder":
        K_List.remove("Blackbird")
        K_List.remove("Rolling Thunder")
    elif K2 == "Chopper Gunner":
        K_List.remove("Chopper Gunner")
    elif K2 == "Attack Dogs" or K2 == "Gunship":
        K_List.remove("Attack Dogs")
        K_List.remove("Gunship")
    
    K3 = random.choice(K_List)
    
    if P1 == "Hardline":
        if Killstreaks[K1] > Killstreaks[K2]:
            if Killstreaks[K1] > Killstreaks[K3]:
                if Killstreaks[K2] > Killstreaks[K3]:
                    print(f"({Killstreaks[K3] - 1}) " + K3)
                    print(f"({Killstreaks[K2] - 1}) " + K2)
                    print(f"({Killstreaks[K1] - 1}) " + K1)
                elif Killstreaks[K2] < Killstreaks[K3]:
                    print(f"({Killstreaks[K2] - 1}) " + K2)
                    print(f"({Killstreaks[K3] - 1}) " + K3)
                    print(f"({Killstreaks[K1] - 1}) " + K1)
            elif Killstreaks[K1] < Killstreaks[K3]:
                print(f"({Killstreaks[K2] - 1}) " + K2)
                print(f"({Killstreaks[K1] - 1}) " + K1)
                print(f"({Killstreaks[K3] - 1}) " + K3)
        elif Killstreaks[K1] < Killstreaks[K2]:
            if Killstreaks[K2] < Killstreaks[K3]:
                print(f"({Killstreaks[K1] - 1}) " + K1)
                print(f"({Killstreaks[K2] - 1}) " + K2)
                print(f"({Killstreaks[K3] - 1}) " + K3)
            elif Killstreaks[K2] > Killstreaks[K3]:
                if Killstreaks[K1] < Killstreaks[K3]:
                    print(f"({Killstreaks[K1] - 1}) " + K1)
                    print(f"({Killstreaks[K3] - 1}) " + K3)
                    print(f"({Killstreaks[K2] - 1}) " + K2)
                elif Killstreaks[K1] > Killstreaks[K3]:
                    print(f"({Killstreaks[K3] - 1}) " + K3)
                    print(f"({Killstreaks[K1] - 1}) " + K1)
                    print(f"({Killstreaks[K2] - 1}) " + K2)

    else:
        if Killstreaks[K1] > Killstreaks[K2]:
            if Killstreaks[K1] > Killstreaks[K3]:
                if Killstreaks[K2] > Killstreaks[K3]:
                    print(f"({Killstreaks[K3]}) " + K3)
                    print(f"({Killstreaks[K2]}) " + K2)
                    print(f"({Killstreaks[K1]}) " + K1)
                elif Killstreaks[K2] < Killstreaks[K3]:
                    print(f"({Killstreaks[K2]}) " + K2)
                    print(f"({Killstreaks[K3]}) " + K3)
                    print(f"({Killstreaks[K1]}) " + K1)
            elif Killstreaks[K1] < Killstreaks[K3]:
                print(f"({Killstreaks[K2]}) " + K2)
                print(f"({Killstreaks[K1]}) " + K1)
                print(f"({Killstreaks[K3]}) " + K3)
        elif Killstreaks[K1] < Killstreaks[K2]:
            if Killstreaks[K2] < Killstreaks[K3]:
                print(f"({Killstreaks[K1]}) " + K1)
                print(f"({Killstreaks[K2]}) " + K2)
                print(f"({Killstreaks[K3]}) " + K3)
            elif Killstreaks[K2] > Killstreaks[K3]:
                if Killstreaks[K1] < Killstreaks[K3]:
                    print(f"({Killstreaks[K1]}) " + K1)
                    print(f"({Killstreaks[K3]}) " + K3)
                    print(f"({Killstreaks[K2]}) " + K2)
                elif Killstreaks[K1] > Killstreaks[K3]:
                    print(f"({Killstreaks[K3]}) " + K3)
                    print(f"({Killstreaks[K1]}) " + K1)
                    print(f"({Killstreaks[K2]}) " + K2)
    print()

generate()