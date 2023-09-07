from main import parsed_data

unique_src_ips = {entry['src_ip_port'].split(':')[0] for entry in parsed_data}
unique_dst_ips = {entry['dst_ip_port'].split(':')[0] for entry in parsed_data}

unique_ips = unique_src_ips.union(unique_dst_ips)
num_unique_ips = len(unique_ips)

print(num_unique_ips)
