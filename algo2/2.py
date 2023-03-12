with open('ET_small.txt', 'r') as file:
    num_tests = int(file.readline().strip())
    test_cases = []
    for _ in range(num_tests):
        num_values = int(file.readline().strip())
        values = []
        for _ in range(num_values):
            values.append(list(map(int, file.readline().strip().split(','))))
        test_cases.append(values)
n=0
for i in test_cases:
  n+=1
  accent_paint=0
  regular_paint=0
  total_hours=0
  for j in i:
    walls=(j[1]*3)+(j[2]*4)+(j[3]*6)
    accent=walls*1/3
    regular=walls*2/3
    accent_paint+=round(accent*1.5,2)
    regular_paint+=regular*2.25
    accent_hours=accent*2.5
    regular_hours=regular*3.25
    total_hours+=accent_hours+regular_hours
  print(f"Case #{n}: "+"%.2f, "%total_hours+"%.2f, "%accent_paint+"%.2f "%regular_paint)