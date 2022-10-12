from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(hostname='192.168.0.63', username='admin', password='admin')
device.open()
print("Connected successfully")

# device.load_merge_candidate(config='interface loopback1003\n ip address 2.1.1.1 255.255.255.0')
device.load_merge_candidate(filename='config.txt')

print(device.compare_config())
if len(device.compare_config()) > 0:
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print("Committing ....")
        device.commit_config()
        choice = input("\nWould you like to Rollback to previous config? [yN]: ")
        if choice == 'y':
            print("Rolling back to previous config ...")
            device.rollback()
    else:
        print("Discarding ...")
        device.discard_config()
else:
    print("No difference")
device.close()
print("Disconnected from the device")