import re

with open('traf.txt', 'r') as f_obj:
    data = f_obj.read()

lines = [line.strip() for line in data.split("\n") if line.strip()]


def is_valid_ipv4(ip):
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    if not pattern.match(ip):
        return False
    return all(map(lambda n: 0 <= int(n) <= 255, ip.split('.')))


def is_valid_mac(mac):
    pattern = re.compile(r'^[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){5}$')
    return bool(pattern.match(mac))


def parse_line(line):
    parts = line.split(';')
    if len(parts) != 7:
        return None

    src_ip_port, src_mac, dst_ip_port, dst_mac, is_udp, data_size, time = parts
    src_ip, _, src_port = src_ip_port.partition(':')
    dst_ip, _, dst_port = dst_ip_port.partition(':')

    if not all([
        is_valid_ipv4(src_ip), src_port.isdigit(), is_valid_mac(src_mac),
        is_valid_ipv4(dst_ip), dst_port.isdigit(), is_valid_mac(dst_mac),
        is_udp in ['true', 'false'], data_size.isdigit(),
        re.match(r'^\d+(\.\d+)?$', time)
    ]):
        return None

    return {
        'src_ip_port': src_ip_port,
        'src_mac': src_mac,
        'dst_ip_port': dst_ip_port,
        'dst_mac': dst_mac,
        'is_udp': is_udp == 'true',
        'data_size': int(data_size),
        'time': float(time)
    }


parsed_data = [parse_line(line) for line in lines]
parsed_data = [entry for entry in parsed_data if entry]
