import pyudev

context = pyudev.Context()

def searchDrives(usbSelect):
    usbSelect.clear()
    for device in context.list_devices(DEVTYPE='disk'):
        if 'ID_USB_DRIVER' in device:
            deviceNode = device.device_node
            model = device.get('ID_MODEL', 'Unknown')
            output = f"{model} ({deviceNode})"
            usbSelect.addItem(output, deviceNode)
            print(f"[WRITEDD] {output}")
