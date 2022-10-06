
schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

print(f"UNC has {schools['UNC']} students")

schools.pop("Duke")

schools["UNC"] = 20000
schools["NCSU"] += 200

# print(schools["UNCC"])

# Example looping over the keys of a dict 

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
