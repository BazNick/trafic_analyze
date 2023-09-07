from main import parsed_data

for entry in parsed_data:
    entry['speed'] = entry['data_size'] / entry['time']

udp_peak_speed = max(entry['speed'] for entry in parsed_data if entry['is_udp'])
tcp_peak_speed = max(entry['speed'] for entry in parsed_data if not entry['is_udp'])

print(udp_peak_speed, tcp_peak_speed, udp_peak_speed > tcp_peak_speed)
