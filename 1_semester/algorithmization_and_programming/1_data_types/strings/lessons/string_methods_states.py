domain1 = "www.yandex.ru"
domain2 = "www.youtube.com"
domain3 = "www.rutracker.org"
domain4 = "yandex.ua"

end = ".ru"
start = "www"

print(domain1.endswith(end))
print(domain2.endswith(end))
print(domain3.endswith(end))
print(domain4.endswith(end))

print(domain1.startswith(start))
print(domain2.startswith(start))
print(domain3.startswith(start))
print(domain4.startswith(start))