import requests as req
import json

s_url = "https://api.hh.ru/specializations"
specs: json = req.get(s_url).json()
with open("main_prof_specs.csv", 'w') as f:
    for vac in specs:
        for vac_sub in vac["specializations"]:
            f.write(vac_sub["id"].split(".")[1] + ";" + vac_sub["name"] + "\n")

with open("specializations.json", "w") as f:
    json.dump(specs, f, ensure_ascii=False)

with open("main_prof_area.csv", 'w') as f:
    for vac in specs:
        f.write(vac["id"] + ";" + vac["name"] + "\n")
