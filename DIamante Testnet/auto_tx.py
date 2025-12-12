import pyautogui
import time
import random

count = int(input("input jumlah transaksi : "))
amount = float(input("input amount transaksi : "))

print("⏳ Starting bot in 5 seconds...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("✅ Bot started!")


addresses = [
    "0x5825e4bad302097ab78a467cd59f208497a2756a",
    "0x8f22f2063d253846b53609231ed80fa571bc0c8f",
    "0xaf41a7623e7ffdf5a337133af7be647746efbd9b",
    "0x7dffd52355ef5e108caa9db94a790531bc87a660",
    "0x8be9227f531db00fb19a4a16825659839595d98c",
    "0x48eea8a13fc962421ebde3ac8c3f88659e5580ac",
    "0x7cbfe7a443cfd23ff97c92ff9c0552ea1f9b1001",
    "0xcafb8d0c5bc88ca3a082161d0bf735beadb9dbda",
    "0xb6564180a6c3a016c4ca46561f56c07f97c32990",
    "0x9e6b4653cb3ed5261c98c660aa953766a20326de",
    "0xa96acc6295aa699b0cd8e23df868f6712b5fc7de",
    "0xec8e8254631c5900c8970c8a5ebb70a32d2e3266",
    "0x8be9227f531db00fb19a4a16825659839595d98c",
    "0x168f89f830dbd6225682ab91fc51ddfb59ea6d30",
    "0xec8e8254631c5900c8970c8a5ebb70a32d2e3266",
    "0xba6bcb74a03361ea390a1b02ef2afd506243f986",
    "0x8f160cec7bc8ac59f77e6f0fce3c02d2decef6b7",
    "0xeef60d057133e4e6783bbd80cd92e93c8fdb5738",
    "0x8be9227f531db00fb19a4a16825659839595d98c",
    "0xd73447a1b90f94fe203e57c63cfb3b5723b2590a",
    "0xec8e8254631c5900c8970c8a5ebb70a32d2e3266",
    "0xF744b161F6Cf24a8743F9f43DBd162636221E175",
    "0xd0e22bc59579625b4fb9d42278f56127dded19a0",
    "0xec8e8254631c5900c8970c8a5ebb70a32d2e3266",
    "0xe62099f47271cf617f0b56b7f07444079e10430e",
    "0x6cfd456cf692725e262ea206850cd92e93203a76",
    "0x5b062e154a221286d8d742b9a2cc3dca296c44cd",
    "0x91212ff5d5b7dd9c94787c4b3fa58628bf1bb446",
    "0x45897a2455241ba387adf23e9c96aa5aac7173a5",
    "0xc99149b8f0a373939c0d52aeb4414ad3a9ac5310",
    "0x4ab9d0818251638469d9b3e58c5746758d843f6d",
    "0x5bfd093e864f30623ff6798af549341e8a7bcfea",
    "0xa28e8ef53c2f6df8e026544ebd22f44f2cb66061",
    "0x0f3b5c92533ace4d42565c80e41b2f4fed6bd32f",
]


for i in range(count):
    print(f"Melakukan transaksi {i + 1} dari {count}...")
    address = addresses[i % len(addresses)]

    pyautogui.click(879, 342)  # tombol send 1
    time.sleep(2)
    msg = random.choice(addresses)
    pyautogui.write(msg, interval=0.05)
    time.sleep(2)

    pyautogui.click(706, 565)  # tombol amount
    pyautogui.write(str(amount), interval=0.05)
    time.sleep(2)

    pyautogui.click(1105, 802)  # tombol send 2
    time.sleep(2)

    pyautogui.click(842, 693)  # maybe
    time.sleep(2)
