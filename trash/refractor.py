import uuid
# # Python code to
# # demonstrate readlines()
  
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
  
# # writing to file


# # Using readlines()
file = open('ips.json', 'r')
Lines = file.readlines()
json = json.replace('{', "{\n" )

with open('ip.json', 'w') as f:
    f.write(json)

count = 0
ip_line =[]
# Strips the newline character
for line in Lines:
    count += 1
    if "ip" in line:
        #ip_line.append(count)
        # replace_line('ips.json', count+3, "{\n\n")import uuid
# print uuid.uuid4()
        replace_line('ip.json', count-2, '"id":'+ '"' + str(uuid.uuid1())+ '"'+',\n')  
    # print("Line{}: {}".format(count, line.strip()))
print(ip_line)

# for line in ip_line:
#     replace_line('ips.json', line, "{\n\n")


# print(json)
print(uuid.uuid4())