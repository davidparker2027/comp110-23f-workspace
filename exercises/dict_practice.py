"""dict practice."""

ice_cream: dict[str, int] = {"Chocolate": 12, "Vanilla": 8, "Strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
ice_cream["Vanilla"] += 2
#  print(len(ice_cream))

#  print("Chocolate" in ice_cream)

for key in ice_cream:
    print(key + " has " + str(ice_cream[key]) + " orders")