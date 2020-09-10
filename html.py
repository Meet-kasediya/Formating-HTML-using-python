print('=====================================================================')
print('                     Registrations open                          ')
print('=====================================================================\n')
import progressbar 
import time 
import webbrowser
  
def prog(): 
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(10): 
        time.sleep(0.1) 
        bar.update(i) 
 
prog() 
 
 
y = input("\t* Name please :\t")
x = input("\t* Your age :\t")
z = input("\t* Work experience (in years) :\t")
a = input("\t* Your gender :\t")
b = input("\t* Applying for :\t")


print('\n')
print('--------------R-E-S-U-L-T-S--------------\n')


if y == "":
 print("Please provide us with a genuine name")
else:
	print('Your name looks right.')	
if a == "":
 print("Please type your gender")
else:
	print(' ')
if b == "":
 print("Please mention for what you are applying")
else:
	print(' ')				
if x == "":
 print("Please provide us with a genuine age")
else:
	print('Your age is approved!')
if z == "":
 print("Please enter your work experience")
else:
	print('Good!, looks like you are all set for the job!')
import progressbar 
import time 
  
    
def prog(): 
      
    widgets = ['Loading Receipt... ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(10): 
        time.sleep(0.1) 
        bar.update(i) 
          

prog() 
print('\n')			
print('---------------Your Receipt--------------')
print('Name: ', y,)	
print('Age: ', x, 'yrs')	
print('Exp.: ', z, 'years experience')
print('Gender: ', a,)
print('Applied for : ', b,)	
print('\n')			
print('-------------ID-----678956345------------')

import progressbar 
import time 
  
  
def prog(): 
      
    widgets = ['Generating invoice…: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(10): 
        time.sleep(0.1) 
        bar.update(i) 
          
prog() 
print('\n')	
print('-----------I-N-V-O-I-C-E-----------')
print('\n')	


cand_record = {
'gender': a,
'name': y,
'cause': b,
'age': x,
'expertise': z,}

cand_statement = '{} who is {} years old {} candidate and claims to have {} year(s) of expertise has applied for \'{}\' in abc.corp'

print(cand_statement.format(cand_record['name'],
                             cand_record['age'],
                             cand_record['gender'],
                             cand_record['expertise'],
                             cand_record['cause']))
print('\n')	
print('---------ID----678956345-----------')


# Creating html file

try:
 my_file = open("my_file.html", "w")        # Open a file	
 my_file.write('<link rel="stylesheet" type="text/css" href="my_file.css">')
 my_file.write('<span ><a href="https://github.com/Meet-kasediya/" target="_blank">Github Files</a></span><hr>')		
 my_file.write('<center><h2>Your Receipt</h2></center><br>')
 my_file.write('<div class="up"><b>Name:<span class="space">  </span> </b>')
 my_file.write(y)
 my_file.write('<br>')	
 my_file.write('<b>Age:<span class="space1"> </b>')	
 my_file.write(x)	 
 my_file.write(' yrs <br>')
 my_file.write('<b>Experience:<span class="space2"> </b>')
 my_file.write(z)	 
 my_file.write(' years experience <br>')	
 my_file.write('<b>Gender:<span class="space3"> </b>')
 my_file.write(a)
 my_file.write('<br>')		
 my_file.write('<b>Applied for: <span class="space5"> </span></b>')	
 my_file.write(b)
 my_file.write('</div><br>')				
 my_file.write('<code> -ID- 678956345 </code><button disabled> COPY </button> ')
 my_file.write('<br><br>')
 my_file.write('<hr><center><h3> I-N-V-O-I-C-E </h3></center><br><center><p class="invoice"> &ldquo; ')
 my_file.write(cand_statement.format(cand_record['name'],
                             cand_record['age'],
                             cand_record['gender'],
                             cand_record['expertise'],
                             cand_record['cause']))
 
 
 my_file.write(" &rdquo;</p></center><br><hr> <button onmouseover='window.location.href=window.location.href'><b> Refresh page </b></button><br>")
 my_file.write('<br> - <font color="grey">Coded By <a href="https://www.linkedin.com/in/meet-kasediya-6308031ab/">Meet Kasediya</a></font>')
except:
  print("Due to some errors your HTML file isn\'t generated!")



 
from tqdm import tqdm 
import time 
  
  
for i in tqdm (range (100),  
               desc="Generating…",  
               ascii=False, ncols=75): 
    time.sleep(0.01) 
      
print("HTML Generated Successfully.\n")
webbrowser.get('windows-default').open('my_file.html')  

print("    ===   ==================================   ==")
print('                 **    Panel ends   **                       ')
print("    ===   ==================================   ==")
 