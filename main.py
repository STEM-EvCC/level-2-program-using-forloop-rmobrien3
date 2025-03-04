mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

T_Missions = len(mission_names)
S_Missions = sum(mission_success)
Before_2000 = []

for i in range(len(mission_names)):
    T_Missions += 1
    if mission_success[i]:
        #successful missions incrimented
        S_Missions += 1
    if mission_years[i] < 2000:
        #as far as I understand it, before_2000.append takes both 
        #mission mame and years, compares the list and appends it to 
        #only list out missions before year 2000
        Before_2000.append(mission_names[i])



#calc's success rate
success_rate = (S_Missions / T_Missions) * 100 
print(f"Total number of missions: {T_Missions}")
print(f"Number of successful missions: {S_Missions}")
print(f"Success rate: {success_rate:.2f}%")
#prints missions launched before 2000 in a list
print("Missions launched before the year 2000: ")
for m in Before_2000:
    print(m)

