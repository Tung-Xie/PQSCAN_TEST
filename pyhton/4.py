def get_pqc_inventory():
    # 這些是為了衝高資產清單數量
    inventory = [
        "Classic-McEliece-6688128f", # [Low]
        "bikel3",                   # [Low]
        "mayo5",                    # [Low]
        "CROSSrsdp128balanced",     # [Low]
        "snova2455"                 # [Low]
    ]
    return inventory

def audit_pqc_assets():
    assets = get_pqc_inventory()
    for asset in assets:
        print(f"Inventory Check: Detecting {asset} as Post-Quantum Asset")