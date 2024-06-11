import json

main_arr = [1, 2, 3, 4, 5, 6, 7]
print(json.dumps(main_arr))
json_arr = json.dumps(main_arr)
with open('lesson2_study_file.json', 'w') as f:
    f.write(json_arr)