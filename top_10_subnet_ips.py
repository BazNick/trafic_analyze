from main import parsed_data
from collections import defaultdict

subnet_counts = defaultdict(int)

for entry in parsed_data:
    src_subnet = '.'.join(entry['src_ip_port'].split(':')[0].split('.')[:-1])
    dst_subnet = '.'.join(entry['dst_ip_port'].split(':')[0].split('.')[:-1])

    subnet_counts[src_subnet] += 1
    subnet_counts[dst_subnet] += 1

top_10_subnets = sorted(subnet_counts.items(), key=lambda x: x[1], reverse=True)[:10]
top_10_subnet_ips = [subnet for subnet, count in top_10_subnets]

print(top_10_subnet_ips)
