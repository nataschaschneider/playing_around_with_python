#Hiring Helper
#The hiring helper can help determining the suitability of a specific candidate to be hired based on specified traits and skills.

#Definitions:

def delay_short(): #time delay for improved readability of output
    i=1
    while i <10000000:
        i=i+1

def delay_long(): #time delay for improved readability of output
    i=1
    while i <60000000:
        i=i+1

def requirement_entry(): #validation of input data integrity
    delay_short()
    your_y=input("Please enter a number:")
    while True:
        try:
            Value=int(your_y)
        except ValueError:
            your_y=input("Please enter a numeric value:")
            continue
        if not(int(your_y)<6 and int(your_y)>0):
            your_y=input("Please enter a valid number. You can refer to the scale above:")
            continue
        break
    return(int(your_y))

def rating(your_y): #calculation of match score
    match=(my_x)/int(your_y)
    if match>=1:
        return(100)
    else:
        return(match*100)

#Intro

print("Hello, I am the HIRING HELPER!\n")

delay_short()

print("I will aid your decision making process in finding a suitable candidate for your data analyst vacancy.\n")

delay_long()

print("To determine if a candidate is a good fit, please help me understand your priorities by answering a few questions.\n")

delay_long()
  
print("""For all questions, please consider the following scale:
1 = not important
2 = beneficial
3 = desired
4 = highly desired
5 = essential
""")

delay_long()

#Trait/skill section

#first class degree in a scientific subject area      
print("How important would you rate a first class degree in a scientific subject area?")
my_x=(5)
your_y=requirement_entry()
delay_short()
score=[rating(your_y)]

#timeliness        
print("How important would you rate timeliness?")
my_x=(4)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#organisational skills      
print("How important would you rate organisational skills?")
my_x=(5)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#attention to detail       
print("How important would you rate attention to detail?")
my_x=(5)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#curiosity for data and how to make sense of it       
print("How important would you rate curiosity for data and how to make sense of it?")
my_x=(5)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#friendliness and team working skills       
print("How important would you rate friendliness and team working skills?")
my_x=(5)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#touble shooting skills       
print("How important would you rate trouble shooting skills?")
my_x=(4)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#data analytics skills      
print("How important would you rate data analytics skills?")
my_x=(3)
your_y=requirement_entry()
delay_short()
score.append(rating(your_y))

#Calculation of final rating
mean=round(sum(score)/len(score),1)
delay_short()

#Final output
print(f"\nNatascha Schneider is a {mean} % match for your requirements.\n Please consider inviting her for an interview!")
