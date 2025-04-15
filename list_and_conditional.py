fav_bands = ["Sales", "Gap Band", "Jannabi", "Tame Impala"]

print(fav_bands)

if "Gap Band" in fav_bands:
    fav_bands.remove("Gap Band")
else :
    fav_bands.insert(1, "Gap Band")

print(fav_bands)
