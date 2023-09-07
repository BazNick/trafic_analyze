from main import parsed_data

total_data = sum(entry['data_size'] for entry in parsed_data)
total_time = sum(entry['time'] for entry in parsed_data)

average_speed = total_data / total_time

print(average_speed)
