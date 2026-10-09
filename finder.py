import requests

target = "http://127.0.0.1:5000"
paths = ["/", "/login", "/admin", "/menu", "/dashboard", "/api"]

print(f"كنقلب على الصفحات المخبية فـ {target}...\n")

for path in paths:
    url = target + path
    try:
        r = requests.get(url, timeout=2)
        if r.status_code == 200:
            print(f"[FOUND] {path} -> موجودة (200 OK)")
        elif r.status_code == 404:
            print(f"[NOT FOUND] {path} -> ما كايناش")
        else:
            print(f"[{r.status_code}] {path}")
    except:
        print(f"[ERROR] ما قدرتش نوصل لـ {path}")

print("\nالخلاصة: الهاكر كيقلب على /admin و /login باش يدخل")