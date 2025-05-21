
# from aes_wrapper import AESWrapper
import wave
global payload_mi 

class DSDState():
    def __init__(self,payload_mi):
        self.currentslot = 0
        self.payload_mi =  payload_mi # القيمة الابتدائية (من أول 4 بايت)
        # self.payload_mi = 0
        self.payload_miR = 0
        self.aes_iv = [0] * 16
        self.aes_ivR = [0] * 16
        self.payload_algid = 0x24
        self.payload_keyid = 0x01
        # self.payload_algid = 0
        # self.payload_keyid = 0
        self.payload_algidR = 0
        self.payload_keyidR = 0
        self.DMRvcL = 0
        self.DMRvcR = 0

def LFSR128d(state: DSDState):
    lfsr = 0
    aes_iv = ''

    if state.currentslot == 0:
        lfsr = state.payload_mi
    else:
        lfsr = state.payload_miR

    # Start packing aes_iv
    if state.currentslot == 0:
        state.aes_iv[0] = (lfsr >> 24) & 0xFF
        state.aes_iv[1] = (lfsr >> 16) & 0xFF
        state.aes_iv[2] = (lfsr >> 8) & 0xFF
        state.aes_iv[3] = (lfsr >> 0) & 0xFF
    elif state.currentslot == 1:
        state.aes_ivR[0] = (lfsr >> 24) & 0xFF
        state.aes_ivR[1] = (lfsr >> 16) & 0xFF
        state.aes_ivR[2] = (lfsr >> 8) & 0xFF
        state.aes_ivR[3] = (lfsr >> 0) & 0xFF

    cnt = 0
    x = 32
    for cnt in range(96):
        # 32, 22, 2, 1
        bit = ((lfsr >> 31) ^ (lfsr >> 21) ^ (lfsr >> 1) ^ (lfsr >> 0)) & 0x1
        lfsr = ((lfsr << 1) | bit) & 0xFFFFFFFFFFFFFFFF  # keep within 64-bit

        # Continue packing aes_iv
        index = x // 8
        if state.currentslot == 0:
            state.aes_iv[index] = ((state.aes_iv[index] << 1) + bit) & 0xFF
        elif state.currentslot == 1:
            state.aes_ivR[index] = ((state.aes_ivR[index] << 1) + bit) & 0xFF
        x += 1

    # Assign next 32-bit short MI
    if state.currentslot == 0:
        next_mi = (
            (state.aes_iv[4] << 24) |
            (state.aes_iv[5] << 16) |
            (state.aes_iv[6] << 8) |
            (state.aes_iv[7] << 0)
        )
    elif state.currentslot == 1:
        next_mi = (
            (state.aes_ivR[4] << 24) |
            (state.aes_ivR[5] << 16) |
            (state.aes_ivR[6] << 8) |
            (state.aes_ivR[7] << 0)
        )

    # Logging and state update
    if state.currentslot == 0:
        print("\033[33m", end='')  # KYEL
        print(" Slot 1", end='')
        print(f" DMR PI C- ALG ID: {state.payload_algid:02X}; KEY ID: {state.payload_keyid:02X}; MI(128): ", end='')
        for byte in state.aes_iv:
            aes_iv = aes_iv +f"{byte:02X}"
        print(f"{aes_iv}", end='')
        print("\033[0m", end='')  # KNRM
        print(";", end='')

        if state.payload_algid == 0x24:
            print(" AES-128;")
        else:
            print(" AES-256;")

        state.payload_mi = next_mi
        state.DMRvcL = 0

    elif state.currentslot == 1:
        print("\033[33m", end='')  # KYEL
        print(" Slot 2", end='')
        print(f" DMR PI C- ALG ID: {state.payload_algidR:02X}; KEY ID: {state.payload_keyidR:02X}; MI(128): ", end='')
        for byte in state.aes_iv:
            aes_iv = aes_iv +f"{byte:02X}"
        print(f"{aes_iv}", end='')
        print("\033[0m", end='')  # KNRM
        print(";", end='')

        if state.payload_algidR == 0x24:
            print(" AES-128;")
        else:
            print(" AES-256;")

        state.payload_miR = next_mi
        state.DMRvcR = 0
    return state.payload_mi,aes_iv
payload_mi = 0