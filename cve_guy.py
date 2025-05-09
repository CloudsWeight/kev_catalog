import os, json, random, time, datetime

def load_cve(json_file='cve_catalog.json'):
    with open(json_file, 'r', encoding='utf8') as f:
        data = json.load(f)
        return data

def search_vulns(term="CISCO devices VLAN"):
    data = load_cve()
    res = []
    vulns = data['vulnerabilities']
    for i in vulns:
        if term in i["shortDescription"] or term in i["vulnerabilityName"]:
            res.append(i)
    if res:
        print(json.dumps(res, indent=2))
        return res
    else:
        print("No results")
        pass


def main():
    data = load_cve()
    search_vulns('firewall')

if __name__ == "__main__":
    main()
