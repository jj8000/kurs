import re

with open("input.txt") as i:
    raw = i.read()

    codes = re.findall(r"\d\d-\d{3}", raw)
    emails = re.findall(r"[\w\d-\.]*@[\w\d-\.]+[\w\d]", raw)
    dates = re.findall(r"[0-3]\d \w{3} \d{4}", raw)

print(codes)
print(emails)
print(dates)