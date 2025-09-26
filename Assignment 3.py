# No-module Python script to find which TV show has the most seasons and most episodes
CSV_PATH = r"c:\Users\sebas\Downloads\TV_show_data.csv"

def to_int_safe(s):
    s = s.strip().strip('"').strip("'")
    try: return int(s)
    except: return 0

def main():
    try:
        f = open(CSV_PATH, encoding="utf-8")
    except Exception as e:
        print("Error:", e); return

    cols = f.readline().strip().split(",")
    try:
        i_name, i_seasons, i_episodes = [cols.index(c) for c in ["Name","Total Seasons","Total Episodes"]]
    except: 
        print("Missing required column"); return

    max_seasons = max_episodes = -1
    season_names = episode_names = []

    for line in f:
        if not line.strip(): continue
        fields = line.strip().split(",")
        if len(fields) < max(i_name,i_seasons,i_episodes)+1: continue

        name = fields[i_name].strip().strip('"')
        seasons, episodes = to_int_safe(fields[i_seasons]), to_int_safe(fields[i_episodes])

        if seasons > max_seasons: max_seasons, season_names = seasons, [name]
        elif seasons == max_seasons: season_names.append(name)

        if episodes > max_episodes: max_episodes, episode_names = episodes, [name]
        elif episodes == max_episodes: episode_names.append(name)

    f.close()

    if max_seasons >= 0:
        print(f"Show(s) with most seasons ({max_seasons}):\n - " + "\n - ".join(season_names))
    else: print("No season data found")

    print()

    if max_episodes >= 0:
        print(f"Show(s) with most episodes ({max_episodes}):\n - " + "\n - ".join(episode_names))
    else: print("No episode data found")

if __name__ == "__main__":
    main()
