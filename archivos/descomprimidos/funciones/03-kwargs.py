def get_product(**datos):
    if "name" in datos:
        print(f"{datos} --> {datos["id"]}, {datos["name"]}")
    else:
        print(f"{datos} --> {datos["id"]}")

get_product(id=6788)
get_product(id=21,
            name="iPhone",
            desc="Esto es un iPhone")