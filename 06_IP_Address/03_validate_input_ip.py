import ipaddress

ip_list = []
while True:
    try:
        ip_input = input(f"\n\n{'~' * 50}\nEnter IP Address/list/exit: ")
        if ip_input == 'exit':
            print("Exiting the script")
            break
        if ip_input == 'list':
            print(f"Current assigned list is: {sorted(ip_list)}")
            continue
        else:
            ip_input = ipaddress.ip_address(ip_input)
        lan_subnet = ipaddress.ip_network("192.168.0.0/24")
        if ip_input not in ip_list:
            if ip_input in lan_subnet:
                ip_list.append(ip_input)
                print("Value accepted: IP Added to the list")
            else:
                print("Subnet mismatch, enter IP in 192.168.0.0/24 Range")
        else:
            print("IP Already exist")

    except ValueError:
        print("Invalid IP")


