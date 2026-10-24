raw_names = ["  luke skywalker ", "", "ALEx", "  maria  ", "kaladin stormblessed", "  kara Thrace"]
clean = []

for name in raw_names:
    if name.strip():
        clean.append(name.strip().title())

print(clean)
