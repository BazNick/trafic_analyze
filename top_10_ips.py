from main import parsed_data
from collections import defaultdict

node_data = defaultdict(lambda: {'total_data': 0, 'total_time': 0})

for entry in parsed_data:
    src_ip = entry['src_ip_port'].split(':')[0]
    dst_ip = entry['dst_ip_port'].split(':')[0]

    node_data[src_ip]['total_data'] += entry['data_size']
    node_data[src_ip]['total_time'] += entry['time']
    node_data[dst_ip]['total_data'] += entry['data_size']
    node_data[dst_ip]['total_time'] += entry['time']

for ip, data in node_data.items():
    data['average_speed'] = data['total_data'] / data['total_time']

top_10_nodes = sorted(node_data.items(), key=lambda x: x[1]['average_speed'], reverse=True)[:10]
top_10_ips = [ip for ip, data in top_10_nodes]

print(top_10_ips)
