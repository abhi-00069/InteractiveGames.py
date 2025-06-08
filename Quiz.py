# Creating Library (;D)
import random
import os
questions=('Q: Which among the following waves is used for communication by artificial satellites?','Q: When the speed of a car is doubled then what should be the braking force of the car to stop it at the same distance?','Q: The mass of a star is two times the mass of the Sun. How will it come to an end?','Q: Rain drops fall from great height. Which among the following statements is true regarding it?','Q: Which of the following statements is true when we see a rainbow?','Q: Cement is made hard by:','Q: What happens when a chemical bond is formed?','Q: Which one of the following metals pollutes the air of a city having a large number of automobiles?','Q: Table salt gets moist during the rainy season because:','Q: Which among the following stage is a suitable indicator when the solution of sodium carbonate is mixed with sulphuric acid?','Q: Milk of Magnesia is a suspension of:','Q: The presence of ozone in the stratosphere is responsible for?','Q: The fundamental particles present in the nucleus of an atom are:','Q: In which of the following substances all carbon atoms are quaternary in nature?','Q: The ratio of pure gold in 18-carat gold is:','Q: The colour of the eye depends upon the pigment present inside?','Q: The ability of the eye to see in the dark is due to the production of a purple pigment known as?','Q: The vitamin most readily destroyed by heat is?','Q: Which one of the following is not a vaccine?','Q: The disease that is caused by a virus is?','Q: The locomotory organ of Amoeba is?','Q: The number of chromosomes present in a normal human being is?','Q: An instrument for measuring blood pressure is called?')
opa=('The frequency of 101 series','Two times(2x)','Neutron Star','Their velocity increases and they fall with the same velocity on the earth','We must face the sun and view it through the raindrops','Dehydration','Energy is always absorbed','Cadmium','NaCl is hygroscopic','Methylene Blue','Magnesium Sulphate','Increasing the average global temperature in recent years','Electrons and protons','Graphite','60%','Cornea','Carotene','Riboflavin','BCG','Typhoid','Pseudopodia','23','Barometer')
opb=('Radio Waves','Four times(4x)','Blackhole','They fall with the same ultimate velocity','The Sun remains behind us and we face the raindrops','Hydration and dissociation of water','Energy is always released','Chromium','NaCl is deliquescent','Methyl red','Magnesium Carbonate','A higher rate of photosynhesis','Protons and neutrons','Diamond','75%','Iris','Rhodopsin','Ascorbic acid','Anti-rabies','Cholera','Parapodia','46','Spirometer')
opc=('A.M.','Half(1/2)','White Dwarf','Their velocity increases and they fall with different velocities on the surface of the earth','In a light rainfall, we will face the Sun','Dissociation of water','More energy is released than is absorbed','Lead','NaCl contains some quantity of NaI','Phenolphthalein','Magnesium Hydroxide','Increasing the penetration of ultraviolet rays to the earth','Neutrons and electrons','Teflon','80%','Rods','Iodopsin','Tocopherol','Polio vaccine','Common cold','Flagella','22','Sphygmomanometer')
opd=('Microwaves','One fourth(1/4)','Red Giant','They fall with the ultimate velocity which is different for different droplets','The sky remains clear and the sun is at a lower position in the sky','Polymerisation','Energy is neither released nor absorbed','Copper','NaCl contains hygroscopic impurities like Mg(Cl)2','Methyl orange','Magnesium Chloride','Supplying oxygen for people travelling in jets','Neutrons and positrons','Naphthalene','90%','Cones','Retinene','Thiamene','Progestrone','Tetanus','Cilia','48','Haemocytometer')
Ans=('D','B','A','D','B','B','A','C','D','D','C','C','B','B','B','B','D','B','D','C','A','B','C')
ans=('d','b','a','d','b','b','a','c','d','d','c','c','b','b','b','b','d','b','d','c','a','b','c')

x=0
done=[99,888]
iflost=0
balance=0
i=0
print("-----------------Welcome to the Quiz-----------------")
name=input("Enter your name : ")
age=input("Enter your age : ")
print(name,", ",end='')
oh=input("Do you want to test your knowledge?(y/n): ")
if oh!='y' :
    print("Asshole")
    exit()
while(True) :
    if len(done)==25 :
        print("Congratulations!! You Won $",balance)
        exit()
    x=random.randint(0,22)
    if x in done :
        continue
    done.append(x)
    i+=1
    if i>0 and i<=10 :
        prize=100000
    if i>10 and i<=20 :
        prize=200000
    if i>20 and i<=23 :
        prize=500000
    if(i!=1) :
        tp=input("PRESS RETURN TO CONTINUE")
    os.system('cls')
    print("Question:-",i,"               Prize : $",prize,"          Your Balance : $",balance)
    print(questions[x])
    print("---Your Options---")
    print("A.",opa[x])
    print("B.",opb[x])
    print("C.",opc[x])
    print("D.",opd[x])
    print("Q. Quit")
    a=input("Your Answer: ")
    if a=='q' or a=='Q' :
        os.system('cls')
        print("Well done(:x)")
        print("You Won: $",balance)
        exit()
    if a!=ans[x] and a!=Ans[x] :
        os.system('cls')
        print("Wrong answer(:C)")
        print("You Won: $",iflost)
        exit()
    if i>=1 and i<=10 :
        iflost=100000
        balance+=iflost
        os.system('cls')
        print("Correct Answer(:D)")
        continue
    if i>10 and i<=20 :
        iflost=200000
        balance+=iflost
    if i>20  :
        iflost=500000
        balance+=iflost
        os.system('cls')
        print("Correct Answer(:D)")
        continue
