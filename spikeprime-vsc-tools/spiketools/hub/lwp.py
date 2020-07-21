import hub
import time
import binascii

class HubType:
  DUPLO_TRAIN_HUB_ID = 32
  BOOST_MOVE_HUB_ID = 64
  POWERED_UP_HUB_ID = 65
  POWERED_UP_REMOTE_ID = 66
  CONTROL_PLUS_LARGE_HUB_ID = 128

_connected_idx = None
def _connect_callback(idx):
  global _connected_idx
  print("Connected: %d" % idx)
  _connected_idx = idx
hub.ble.callback(_connect_callback)

def _hexlify(bytes):
  return binascii.hexlify(bytes, ' ').decode()

class LWPButton:
  def __init__(self):
    self._callback = None
    self._pressed = False
    self._was_pressed = False
    self._last_pressed_ms = 0
  def on_change(self, cb):
    self._callback = cb
  def is_pressed(self):
    return self._pressed
  def was_pressed(self):
    r = self._was_pressed
    self._was_pressed = False
    return r
  def _change(self, value):
    if self._pressed != value:
      self._pressed = value
      if value:
        self._was_pressed = True
        self._last_pressed_ms = time.ticks_ms()
        if self._callback:
          self._callback(0)
      else:
        if self._callback:
          l = time.ticks_diff(time.ticks_ms(), self._last_pressed_ms)
          self._callback(l if l > 0 else 1)

class LWPObject:
  pass

class LWPDevice:
  def __init__(self, conn, model_id, idx):
    self.conn = conn
    self.idx = idx
    self.model_id = model_id
    self.conn.callback(self.recv)
    self.conn.subscribe()
    self.button = LWPObject()
    time.sleep(.1)
    if model_id == HubType.DUPLO_TRAIN_HUB_ID:
      self.ledPort = 0x11
    elif model_id == HubType.POWERED_UP_REMOTE_ID:
      self.button.A = LWPObject()
      self.button.B = LWPObject()
      self.button.A.plus = LWPButton()
      self.button.A.red = LWPButton()
      self.button.A.minus = LWPButton()
      self.button.B.plus = LWPButton()
      self.button.B.red = LWPButton()
      self.button.B.minus = LWPButton()
      self.ledPort = 0x34
      self.portMode(0, 3)
      self.portMode(1, 3)
    else:
      self.ledPort = 0x32
    self.button.green = LWPButton()
    self.subscribeToHubProp(2)

  def disconnect(self):
    self.conn.disconnect(self.idx)

  def recv(self, data):
    msg_type = data[2]
    if msg_type == 0x82: # command feedback
      print("cmd output feedback %d: port %02x status %02x" % (self.idx, data[3], data[4]))
    elif msg_type == 0x05: # error
      print("error %d: cmd %02x code %02x" % (self.idx, data[3], data[4]))
    elif msg_type == 0x45: # port value (single)
      port = data[3]
      print("port value %d: port %02x" % (self.idx, port), _hexlify(data[4:]))
      if self.model_id == HubType.POWERED_UP_REMOTE_ID and port < 2:
        b = self.button.A if port == 0 else self.button.B
        b.plus._change((data[4] >> 0) & 1)
        b.red._change((data[4] >> 1) & 1)
        b.minus._change((data[4] >> 2) & 1)
    elif msg_type == 0x47: # port input format (single)
      interval = int.from_bytes(data[5:8], 'little', False)
      print("port mode %d: port %02x mode %02x notify %02x interval %d" % (self.idx, data[3], data[4], data[9], interval))
    elif msg_type == 0x01: # hub property update
      print("hub action %d: prop %02x value" % (self.idx, data[3]), _hexlify(data[5:]))
      if data[3] == 2:
        self.button.green._change(data[5])
    elif msg_type == 0x02: # hub action
      print("hub action %d: %02x" % (self.idx, data[3]))
    elif msg_type == 0x04: # port event
      port = data[3]
      event = data[4]
      if event == 0x00: # detach
        print("port detached %d: %02x" % (self.idx, port))
      elif event == 0x01: # attach
        id = int.from_bytes(data[5:6], 'little', False)
        print("port attached %d: port %02x type %04d" % (self.idx, port, id))
      elif event == 0x02: # attach virtual
        id = int.from_bytes(data[5:6], 'little', False)
        print("port attached virtual %d: port %02x type %04x %02x + %02x" % (self.idx, port, id, data[7], data[8]))
    else:
      print("recv data %02x: " % data[2], self.idx, _hexlify(data[3:]))

  def send(self, data):
    self.conn.send((len(data)+2).to_bytes(2, 'little') + data)
    time.sleep(.2)

  def writePort(self, port, mode, data):
    self.send(bytes([0x81, port, 0x11, 0x51, mode]) + data)

  def writePort1(self, port, mode, b):
    self.writePort(port, mode, bytes([b & 255]))

  def portMode(self, port, mode, notify = 1):
    self.send(bytes([0x41, port, mode, 1, 0, 0, 0, notify]))

  def setHubProp(self, prop, data):
    self.send(bytes([0x01, prop, 0x01]) + data)

  def getHubProp(self, prop):
    self.send(bytes([0x01, prop, 0x05]))

  def subscribeToHubProp(self, prop):
    self.send(bytes([0x01, prop, 0x02]))

  def off(self):
    self.send(bytes([0x02, 0x01]))

  def led(self, *args):
    if len(args) == 1:
      self.portMode(self.ledPort, 0, 0)
      self.writePort1(self.ledPort, 0, args[0])
    elif len(args) == 3:
      self.portMode(self.ledPort, 1, 0)
      self.writePort(self.ledPort, 1, bytes(args))

def connect(timeout = 15):
  global _connected_idx
  hub.ble.scan(timeout)
  for _ in range(timeout):
    for i, a in enumerate(hub.ble.scan_result()):
      if a['service_id'] == '00001623-1212-EFDE-1623-785FEABCD123':
        hub_model_id = a['man_data'][1] if len(a['man_data']) > 1 else None
        print("Connecting to hub model %d" % hub_model_id)
        _connected_idx = None
        conn = hub.ble.connect(i)
        for _ in range(30):
          if _connected_idx != None:
            print('waited: %d' % _)
            break
          time.sleep(.1)
        if conn and _connected_idx != None:
          print("Connected")
          time.sleep(1)
          return LWPDevice(conn, hub_model_id, _connected_idx)
        print('Connection timed out')
        return None
    time.sleep(1)
  return None
