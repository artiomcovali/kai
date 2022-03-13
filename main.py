# termional cd: cd /Users/artiomcovali/Desktop/HackVCIS

import smtplib, ssl, time

age = ""
weight = ""
height = ""
gender = ""
allergies = []
again = "no"
print("""      
 ___  __    ________  ___                        
|\  \|\  \ |\   __  \/\  \    
\ \  \/  /|\ \  \|\  \ \  \   
 \ \   ___  \ \   ___ \ \  \  
  \ \  \ \ \  \ \  \ \ \ \  \                       
   \ \__\ \ \__\ \__\ \_\ \__\ 
    \|__| \|__|\ |__|\|__|\|__|

                (\____/)
                 (_oo_)
                   (O)
                 __||__    \)
              []/_______\[] /
            /   \______/ \/
            /    -/__\-
            (\  -/____\-         
""")

print("Hi I'm Kai, your personal healthcare assistant. I can help you book appointments with your doctor and answer any medical question you have.\nLet me start by getting to know you better!\n")

name = input("\nWhat should I call you?: ")
print(name + ", what a beautiful name!")
receiver_email = input("What is your preffered email?: ")
age = int(input("\nHow old are you?: "))
print("What a cool age! I wish I was " + str(age) + " years old.")
height = int(input("\nWhat about your height (cm)?: "))

weight = input("\nAwesome. How much do you weigh (kg)?: ")
gender = input("\nOkay, and what is your sex? (male/female): ")

allergic = input("\nPerfect. Are you allergic to anything? (yes/no): ")
if allergic.lower() == "no":
    print("\nGreat, having no allergies is a blessing.\nThanks for telling me more about you!")
elif allergic.lower() == "yes":
    allergens = input("\nAww that sucks. What are you allergic to?: ")
    allergies.append(allergens)
    print("\nCool. Thanks for telling me more about you!")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def userProblem():
    problem = input("\nNow what seems to be your problem? What's hurting or bothering you?: ")
    problem = problem.lower()

    if "head hurts" in problem or "headache" in problem or "head pain" in problem or "headaches" in problem or "head pains" in problem or "head hurt" in problem:
        headPain = input("\nHeadaches are very common so there should be nothing to worry about. How bad does it hurt on a scale from 1-10?: ")
        if int(headPain) <= 3 and int(headPain) < 4:
            print("\nSounds like your head doesn't hurt too bad. Try getting some rest and drinking water. If it still hurts after some time you can take some over the counter medication such as Advil or Tylenol.")
        elif int(headPain) <= 6 and int(headPain) > 3:
            print("\nLooks like your headache is pretty severe but don't worry it's probably nothing serious. You should definitely take some pain relief medication such as Advil or Tylenol and try to stay away from screens. You should get some rest and make a cold compress and put it on your forehead. If none of that helps seek medical attention.")
        elif int(headPain) >= 7:
            print("\nYour headache is extremely severe. This could potentially be very dangerous but right now you should take pain killers such as Advil or Tylenol, get some rest, and drink lots of water. Make a cold compress and put it on your forehead. If it still hurts after a couple of hours go to your doctor or the ER.")

        #sends email to patient
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login("kaihealthassistant@gmail.com", "HackVCIS123!")

            subject = 'Regarding your headaches'
            body = f"""
                Hey {name}, I heard you had a headache. Don't worry there's nothing to worry about. Here are some steps you can take to feel better.
                
                1. Take painkillers such as Advil or Tylenol
                    ~ Considering you are {age} years old and weigh {weight} kg you should take 2 pills of Advil or Tylenol
                2. Get plenty of rest
                3. Stay hydrated
                4. Make a cold compress and put it on your forehead
                5. Considering you are a female you could also be on your menstrual cycle meaning your stomach pains could just be cramps
                    ~ You can place a warm heating pad on the areas that are cramping ot help soothe the pain
                6. Lastly, if nothing makes you feel better I can always schedule a doctors appointment for you

                Hope you feel better!
            
                - Your personal healthcare assisant, Kai
                       (\____/)
                        (_oo_)
                          (O)
                        __||__    \)
                     []/_______\[] /
                    /   \______/ \/
                    /    -/__\-
                    (\  -/____\-          
                """
            
            
                
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("kaihealthassistant@gmail.com", receiver_email, msg)
            
            
        print(f"\nIn case you forget what I told you I have sent an email to {receiver_email} with instruction on what to do about your headache along with some prescribed doses.")
        print("(Note: please check your spam folder as the email will most likely be in there)")
    elif "stomach hurts" in problem or "stomachache" in problem or "stomach pain" in problem or "stomachaches" in problem:
        print("\nIt seems you have some stomach or abdominal pain. No need to worry as this can be easily treated.\nMake sure you are staying hydrated and avoid laying on your abdomin. If the pain doesn't go away after some time make sure to take some over the counter medicine such as Pepto Bismol.")
        if gender.lower() == "female":
            print("\nSince you are a female there could be a possiblity that you are currently on your menstrual cycle and the pain you are experincing is cramps caused by your period.\nIf you think this is the case, you can place a heating pad on the area that is cramping up.")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login("kaihealthassistant@gmail.com", "HackVCIS123!")

            subject = 'Regarding your stomach pain'
            if gender.lower() == "female":
                body = f"""
                Hey {name}, I heard you had stomach pain. Don't worry there's nothing to worry about. Here are some steps you can take to feel better.
                
                1. Drink plenty of fluids and stay hydrated
                2. Get some rest
                3. Take medication like Pepto Bismol
                ~ Since you are {age} years old and weigh {weight} kg you should take 30 mL every 30 mintues untill you feel better again
                4. Avoid laying or resting on your stomach
                5. Since you are a female you could possibly be on your menstrual cycle and your stomach pain are just cramps
                ~ You can place a warm heating pad on the area that is cramping to help soothe the pain
                6. Lastly, if nothing makes you feel better I can always schedule a doctors appointment for you

                Hope you feel better!
            
                - Your personal healthcare assisant, Kai
                        (\____/)
                         (_oo_)
                           (O)
                         __||__    \)
                     [] /______\[] /
                    /   \______/ \/
                    /    -/__\-
                    (\  -/____\-          
            """
            elif gender.lower() == "male":
                body = f"""
                Hey {name}, I heard you had stomach pain. Don't worry there's nothing to worry about. Here are some steps you can take to feel better.
                
                1. Drink plenty of fluids and stay hydrated
                2. Get some rest
                3. Take medication like Pepto Bismol
                ~ Since you are {age} years old and weigh {weight} kg you should take 30 mL every 30 mintues untill you feel better again
                4. Avoid laying or resting on your stomach
                5. Since you are a female you could possibly be on your menstrual cycle and your stomach pain are just cramps
                ~ You can place a warm heating pad on the area that is cramping to help soothe the pain
                6. Lastly, if nothing makes you feel better I can always schedule a doctors appointment for you

                Hope you feel better!
            
                - Your personal healthcare assisant, Kai
                        (\____/)
                         (_oo_)
                           (O)
                         __||__    \)
                     [] /______\[] /
                    /   \______/ \/
                    /    -/__\-
                    (\  -/____\-          
            """
                
                
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("kaihealthassistant@gmail.com", receiver_email, msg)
        print(f"\nIn case you forget what I told you I have sent an email to {receiver_email} with instructions on what to do about your stomach pain along with some prescribed doses.")
        print("(Note: please check your spam folder as the email will most likely be in there)")
    elif "back hurts" in problem or "back pain" in problem or "back hurt" in problem or "back aches" in problem:
        print("\nBack pain is one of the most common pains so there is nothing to worry about.")
        print(f"\nFirst you should try to stretch your back muscles to loosen them which will help your pain. You should also rest and not put any stress on your back for at least 4 days. If none of that helps you can take pain relief medicine suich as Ibuprofen. Since you are {age} years old and weight {weight} kg you should take 1200 mg per day.")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login("kaihealthassistant@gmail.com", "HackVCIS123!")

            subject = 'Regarding your back pain'
            body = f"""
                Hey {name}, I heard you had back pain. Don't worry there's nothing to worry about. Here are some steps you can take to feel better.
                
                1. Strech your back to loosen up your muscles
                2. Get some rest and avoid putting stress on your back
                3. Stay hydrated
                4. If nothing helps take pain relioef medicine such as Ibuprofen
                ~ Since you are {age} years old and weigh {weight} kg you should take 1200 mg per day
                5. Lastly, if nothing makes you feel better I can always schedule a doctors appointment for you

                Hope you feel better!
            
                - Your personal healthcare assisant, Kai
                        (\____/)
                         (_oo_)
                           (O)
                         __||__    \)
                     []/_______\[] /
                    /   \______/ \/
                    /    -/__\-
                    (\  -/____\-          
                """
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("kaihealthassistant@gmail.com", receiver_email, msg)
        print(f"\nIn case you forget what I told you I have sent an email to {receiver_email} with instructions on what to do about your back pain along with some prescribed doses.")
        print("(Note: please check your spam folder as the email will most likely be in there)")
    elif "throat hurts" in problem or "sore throat" in problem or "hoarse throat" in problem or "throat pain" in problem:
        print("\nHaving a sore throat is most commonly linked to having a common cold however there are many other viruses that cause a sore throat. Since it is hard for me to tell what exactly caused your sore throat virtually, I will book an apointment with your doctor so they can check you out.")
        print("In the mean time make sure to drink lots of fluids and garge with salt water. If you are coughing, try sucking on cough drops to soothe your throat or eating a popsicle to make your throat feel better. If the pain is still unbearable you can take some cough syrup medicine such as Nyquill or Robitussin.")  
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login("kaihealthassistant@gmail.com", "HackVCIS123!")

            subject = 'Regarding your sore throat'
            body = f"""
                Hey {name}, I heard you had a sore throat. Don't worry there's nothing to worry about. 
                I have booked you an appointment with your doctor so they can check you out and tell you exactly what caused your sore throat.
                In the mean time, here are some steps you can take to feel better:

                1. Drink lots of fluids and stay hydrated
                2. Gargle with salt water
                3. Eat cough drops and/or eat popsicles
                4. If nothing helps take cough syrup such as Nyquill or Robitussin
                ~ Since you are {age} years old and weigh {weight} kg you should take 60 mg every six hours

                Hope you feel better!
            
                - Your personal healthcare assisant, Kai
                         (\____/)
                          (_oo_)
                            (O)
                         __||__    \)
                     []/_______\[] /
                    /   \______/ \/
                    /    -/__\-
                    (\  -/____\-          
                """
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("kaihealthassistant@gmail.com", receiver_email, msg)
        print(f"\nI have booked you an appointment with your doctor and sent an email to {receiver_email} with a confirmation along with instructions on what you can do to treat your sore throat")
        print("(Note: please check your spam folder as the email will most likely be in there)")
    elif "appointment" in problem or "schedule" in problem:
        date = input("I see you would like me to schedule a doctors a appointment. I'll do that right away for you! What date would you prefer for the appointment? (mm/dd): ")
        print(f"Perfect, I will be setting up a doctors appointment for you on {date}")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login("kaihealthassistant@gmail.com", "HackVCIS123!")

            subject = 'Doctors appointment'
            body = f"""
                Hey {name}, upon your request I have scheduled a doctors appointment for you on {date}. 
                Your doctor will check up on you and find out if you have any problems.

                Hope everything goes well!
            
                - Your personal healthcare assisant, Kai
                         (\____/)
                          (_oo_)
                            (O)
                         __||__    \)
                     []/_______\[] /
                    /   \______/ \/
                    /    -/__\-
                    (\  -/____\-          
                """
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("kaihealthassistant@gmail.com", receiver_email, msg)
        print(f"I have sent an email to {receiver_email} and to your doctor confirming that you have a doctors appointment on {date}!")
        print("")
    else:
        print("Sorry it looks like I don't know how to answer that.")

userProblem()

while again.lower() == "no":
    again = input("\nWould that be it for you today? (yes/no): ")
    if again.lower() == "yes":
        print(f"\nIt was a pleasure helping you today, {name}. I hope you have a wonderful rest of your day. Goodbye!")
        quit()
    if again.lower() == "no":
        userProblem()

