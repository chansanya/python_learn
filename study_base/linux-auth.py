import re
from collections import defaultdict
from ipwhois import IPWhois


def getIpInfo(str):
    pattern = r"from (\d+\.\d+\.\d+\.\d+) port (\d+)"
    # 在日志行中查找匹配项
    match = re.search(pattern, str)
    if match:
        ip_address = match.group(1)
        port = match.group(2)
        return {
            "ip": ip_address,
            "port": port
        }
    else:
        return None


def info(ip_address):
    print(f"获取:{ip_address}")
    return IPWhois(ip_address).lookup_rdap()


ip_list = defaultdict(lambda: {"ip": "", "port": "", "count": 0})

with open("./secure", encoding='utf-8') as log:
    log_content = log.readlines()

for line in log_content:
    if 'Failed password' in line:
        ip_info = getIpInfo(line)
        if ip_info and "ip" in ip_info:
            ip = ip_info["ip"]
            count = ip_list[ip]["count"]
            if count == 0:
                ip_list[ip]["ip"] = ip
                ip_list[ip]["port"] = ip_info["port"]
                ip_whois = info(ip)
                ip_list[ip]["info"] = {
                    'asn_registry': ip_whois.get("asn_registry"),
                    'asn': ip_whois.get("asn"),
                    'asn_cidr': ip_whois.get('asn_cidr'),
                    'asn_country_code': ip_whois.get('asn_country_code'),
                    'asn_date': ip_whois.get('asn_date'),
                    'asn_description': ip_whois.get('asn_description')
                }
            ip_list[ip]["count"] = count + 1

sorted_ip_list = sorted(ip_list.values(), key=lambda x: x["count"], reverse=True)
print(sorted_ip_list)
