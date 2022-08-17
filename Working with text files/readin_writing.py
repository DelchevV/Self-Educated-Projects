with open ('test_copy.txt', 'r+') as rf:
    with open("proper_test.txt",'w') as wf:
        for line in rf:
            corrected_line=line.replace(" ",",")
            wf.write(corrected_line)

html_output='<!DOCTYPE html>\n<html lang="en">'

result={}
with open("proper_test.txt",'r') as text:
    for line in text:
        entry=line.split(",")
        email=entry[0]
        identy=entry[1]
        one_time=entry[2]
        recovery=entry[3]
        f_name=entry[4]
        l_name=entry[5]
        location=entry[7]
        result[identy]=[f_name,l_name,email,location,one_time,recovery]
html_output+='\n<ol>'
for key in result:
    html_output+=f"\n<li> {result[key][0]} {result[key][1]} -> Email: {result[key][2]} </li>"
html_output+='\n</ol>'
html_output+='\n</html>'
print(html_output)
with open("file.html",'w') as wf:
    wf.write(html_output)



