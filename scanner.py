import socket

target = input("دخل IP باش تسكاني (مثلا 127.0.0.1): ")

print(f"\nكندير سكان لـ {target} فالـ ports 4900-5100...")

open_ports = []
for port in range(4900, 5101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN - كاين شي حاجة خدامة هنا")
        open_ports.append(port)
    s.close()

print(f"\nالخلاصة: لقينا {open_ports} مفتوحين فالـ range 4900-5100")
if 5000 in open_ports:
    print(">>> هادي هي Café Atlas ديالك! برافو!")