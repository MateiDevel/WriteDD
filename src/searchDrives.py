import pyudev
import threading

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block', device_type='disk')

def searchDrives(usbSelect):
    usbSelect.clear()
    for device in context.list_devices(DEVTYPE='disk'):
        if 'ID_USB_DRIVER' in device:
            deviceNode = device.device_node
            model = device.get('ID_MODEL', 'Unknown')
            output = f"{model} ({deviceNode})"
            usbSelect.addItem(deviceNode)
            print(f"[WRITEDD] {output}")
                          
    def watch():
        for device in iter(monitor.poll, None):
            if 'ID_USB_DRIVER' not in device:
                continue
            if device.action == 'add':
                print(f"[WRITEDD] USB inserted: {device.device_node}")
                searchDrives(usbSelect)
            elif device.action == 'remove':
                print(f"[WRITEDD] USB removed: {device.device_node}")
                searchDrives(usbSelect)

    threading.Thread(target=watch, daemon=True).start() # run in a different thread so gui doesnt freeze