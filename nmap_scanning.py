# Написать программу на Python, которая будет проводить сканирование с использованием nmap.

import nmap3
import json

nmap = nmap3.NmapScanTechniques()
results = nmap.nmap_syn_scan("yandex.ru")

with open('output.json', 'w') as file:
    json.dump(results, file)
