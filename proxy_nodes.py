from main import parsed_data
from collections import defaultdict

communication_data = defaultdict(
    lambda: defaultdict(lambda: {'UDP': {'send': 0, 'receive': 0}, 'TCP': {'send': 0, 'receive': 0}}))

for entry in parsed_data:
    src_ip = entry['src_ip_port'].split(':')[0]
    dst_ip = entry['dst_ip_port'].split(':')[0]
    protocol = 'UDP' if entry['is_udp'] else 'TCP'

    communication_data[src_ip][dst_ip][protocol]['send'] += entry['data_size']
    communication_data[dst_ip][src_ip][protocol]['receive'] += entry['data_size']

proxy_nodes = []
for node, communications in communication_data.items():
    potential_proxy_for = []
    for peer, protocols in communications.items():
        for protocol, actions in protocols.items():
            if actions['send'] > 0 and actions['receive'] > 0:
                potential_proxy_for.append((peer, protocol))
    if len(potential_proxy_for) > 1:
        proxy_nodes.append(node)

print(proxy_nodes)
