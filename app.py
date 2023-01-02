from experta import *
from colorama import init,Fore

DEBUG_MODE=True

class SleepingQuality(Fact):
    # a4, b4, b5, b7
    pass

class EatingHabit(Fact):
    # a2, b2
    pass

class MindCondition(Fact):
    # a1, a5, b1, b6
    pass

class DepressionSymptoms(Fact):
    # c1, c2, c3, c4
    pass

class State(Fact):
    action=Field(str, mandatory=True) # Interviewing / Concluding
    number=Field(int, mandatory=True) # Question Number

class MentalHealthConsultant(KnowledgeEngine):
    @DefFacts()
    def init_state(self):
        yield State(action='menu', number=0)

    # Main Menu
    @Rule(AS.f << State(action='menu', number=0))
    def main_menu(self, f):
        print('Mental Health Consultant')
        print('========================')
        print('1. Consult')
        print('2. About')
        print('3. Exit')
        self.declare(Fact(menu=input(">>")))

    @Rule(AND(
        AS.f1 << Fact(menu='1'),
        AS.f2 << State(action='menu', number=0)
    ))
    def consult(self, f1, f2):
        self.retract(f1)
        self.retract(f2)
        self.declare(State(action='interviewing', number=1))

    @Rule(AND(
        AS.f1 << Fact(menu='2'),
        AS.f2 << State(action='menu', number=0)
    ))
    def about(self, f1,f2):
        self.retract(f1)
        self.retract(f2)
        print("""About Us
=======================
After Pandemic COVID-19, people will eventually face many changes in their life.
Everyone will be forced to adapt from being in online condition to offline.
People who find difficulties will be stressed after having to adapt in a very short time.
People who find it more comfortable having work from home will also feel stressed about going to office.
But, not everyone will realize they have problem with stress and depression.
Our Program give solution to help people find out if they're depressed or in needs for psychiatrist.

This Expert System program will ask for some general life habit in 2 weeks.
Our referrence for the interview is from articles in National Institute of Mental Health's Website
This program is made by a group of iSTTS Student named Mikhael Chris(220116890) and Daniel Gamaliel Saputra(220116870)
The referrence from this program can be read from:
https://www.nimh.nih.gov/health/publications/my-mental-health-do-i-need-help
https://www.nimh.nih.gov/health/publications/depression""")
        input("Click Enter to continue...")
        self.declare(State(action='menu', number=0))

    # Interview & Consultation
    @Rule(AS.f << State(action='interviewing', number=1))
    def a1(self, f):
        while(True):
            x = input('Are you feeling down? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=2))
        self.declare(MindCondition(down=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=2))
    def a2(self, f):
        while(True):
            x = input('Are you eating well? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=3))
        self.declare(EatingHabit(well=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=3))
    def a3(self, f):
        while(True):
            x = input('Are you having hard time to wake up? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=4))
        self.declare(SleepingQuality(dysania=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=4))
    def a4(self, f):
        while(True):
            x = input('Are you having difficulty in concentrating? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=5))
        self.declare(MindCondition(concentraton_difficulty=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=5))
    def b1(self, f):
        while(True):
            x = input('Are you losing interest in things you usually do? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=6))
        self.declare(MindCondition(lose_interest=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=6))
    def b2(self, f):
        while(True):
            try:
                x = int(input('How many times do you usually eat in a day? [number] : '))
                break
            except:
                print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=7))
        self.declare(EatingHabit(frequency=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=7))
    def b3(self, f):
        while(True):
            try:
                x = int(input('How would you are your average sleeping quality? [1-10] : '))
                break
            except:
                print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=8))
        self.declare(SleepingQuality(quality=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=8))
    def b4(self, f):
        while(True):
            try:
                x = int(input('How long do you sleep? (in hours) [number] : '))
                break
            except:
                print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=9))
        self.declare(SleepingQuality(duration=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=9))
    def b5(self, f):
        while(True):
            try:
                x = int(input('How long do you work everyday? (in hours) [number] : '))
                break
            except:
                print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=10))
        self.declare(MindCondition(work_hour=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=10))
    def b6(self, f):
        while(True):
            x = input('Do you get any difficulties in sleeping? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=11))
        self.declare(SleepingQuality(insomnia=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=11))
    def c1(self, f):
        while(True):
            x = input('Do you notice unwanted changes in your body (weights, fatigue, headache, digestion problem, etc)? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=12))
        self.declare(DepressionSymptoms(physic_changes=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=12))
    def c2(self, f):
        while(True):
            x = input('Do you get emotional easily? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=13))
        self.declare(DepressionSymptoms(emotional=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=13))
    def c3(self, f):
        while(True):
            x = input('Have you ever thought of harming yourself? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=14))
        self.declare(DepressionSymptoms(selfharm=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    @Rule(AS.f << State(action='interviewing', number=14))
    def c4(self, f):
        while(True):
            x = input('Have you even thought of suicide/death? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='concluding', number=0)) # Change to conclude
        self.declare(DepressionSymptoms(death=x))
        if DEBUG_MODE==True:
            print(Fore.GREEN + str(es.facts))

    # Conlusion -> Example
    
    @Rule(
        OR(
            AND(
                DepressionSymptoms(physic_changes='y'),
                DepressionSymptoms(emotional='y')
            ),
            DepressionSymptoms(selfharm='y'),
            DepressionSymptoms(death='y'),
        ),
        MindCondition(down=MATCH.a0),
        EatingHabit(well=MATCH.a1),
        SleepingQuality(dysania=MATCH.a2),
        MindCondition(concentraton_difficulty=MATCH.a3),
        MindCondition(lose_interest=MATCH.a4),
        EatingHabit(frequency=MATCH.a5),
        SleepingQuality(quality=MATCH.a6),
        SleepingQuality(duration=MATCH.a7),
        MindCondition(work_hour=MATCH.a8),
        SleepingQuality(insomnia=MATCH.a9),
        DepressionSymptoms(physic_changes=MATCH.a10),
        DepressionSymptoms(emotional=MATCH.a11),
        DepressionSymptoms(selfharm=MATCH.a12),
        DepressionSymptoms(death=MATCH.a13),
        TEST(lambda a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13 : (1 if a0!='n' else 0 )+ (1 if a1!='y' else 0 )+ (1 if a2!='n' else 0 )+ (1 if a3!='n' else 0 ) + (1 if a4=='y' else 0) + (1 if a5<3 else 0) + (1 if a6<6 else 0) + (1 if a7<5 else 0) + (1 if a8<8 else 0) + (1 if a9=='y' else 0) + (1 if a10=='y' else 0 )+ (1 if a11=='y' else 0 )+ (1 if a12=='y' else 0 )+ (1 if a13=='y' else 0 ) >= 10)
    )
    def r3(self):
        print("You are very depressed!")
        print("Please try to consult with doctors or psychiatrist.")
        print("Try to be closer with family and friends")
        print("Take some day off from work so you can remove your burden")
        print("Maintain healthy life and seek help from people close to you")
        print("If you are thinking of self harming or suicide, please stop and rethink about your loved one")
        exit()

    @Rule(OR(
        AND(
            OR(
                MindCondition(concentration_difficulty='y'),
                MindCondition(down='y'),
            ),
            MindCondition(work_hour=P(lambda x: x>8)),
            OR(
                DepressionSymptoms(physic_changes='y'),
                DepressionSymptoms(emotional='y')
            ),
            OR(
                SleepingQuality(quality=P(lambda x: x<6)),
                SleepingQuality(duration=P(lambda x: x<5)),
                SleepingQuality(insomnia='y'),
            )
        ),
        FORALL(
            MindCondition(down=MATCH.a0),
            EatingHabit(well=MATCH.a1),
            SleepingQuality(dysania=MATCH.a2),
            MindCondition(concentraton_difficulty=MATCH.a3),
            MindCondition(lose_interest=MATCH.a4),
            EatingHabit(frequency=MATCH.a5),
            SleepingQuality(quality=MATCH.a6),
            SleepingQuality(duration=MATCH.a7),
            MindCondition(work_hour=MATCH.a8),
            SleepingQuality(insomnia=MATCH.a9),
            TEST(lambda a0,a1,a2,a3,a4,a5,a6,a7,a8,a9 : (1 if a0!='n' else 0 )+ (1 if a1!='y' else 0 )+ (1 if a2!='n' else 0 )+ (1 if a3!='n' else 0 ) + (1 if a4=='y' else 0) + (1 if a5<3 else 0) + (1 if a6<6 else 0) + (1 if a7<5 else 0) + (1 if a8<8 else 0) + (1 if a9=='y' else 0) >= 5)
        )
    ))
    def r2(self):
        print("You are depressed!")
        print("To reduce the depression, you are advised to maintain regular bedtime and eat well.")
        print("You can exercise regularly and hang out with family or friends")
        print("Just do what you have to do and what's important for yourself")
        print("Don't make any important decision that will affect your life")
        exit()

    @Rule(
        MindCondition(down=MATCH.a0),
        MindCondition(lose_interest=MATCH.a1),
        EatingHabit(frequency=MATCH.a2),
        SleepingQuality(quality=MATCH.a3),
        SleepingQuality(duration=MATCH.a4),
        MindCondition(work_hour=MATCH.a5),
        SleepingQuality(insomnia=MATCH.a6),
        TEST(lambda a0,a1,a2,a3,a4,a5,a6 : (1 if a0=='y' else 0) + (1 if a1=='y' else 0) + (1 if a2<3 else 0) + (1 if a3<6 else 0) + (1 if a4<5 else 0) + (1 if a5<8 else 0) + (1 if a6=='y' else 0) > 3 )
    )
    def r1(self):
        print("You have slight stress!")
        print("To reduce the stress you can spend more time with family or go on a short vacation.")
        print("You can also exercise regularly and hang out with friends")
        exit()

    @Rule(
        MindCondition(down=MATCH.a0),
        EatingHabit(well=MATCH.a1),
        SleepingQuality(dysania=MATCH.a2),
        MindCondition(concentraton_difficulty=MATCH.a3),
        TEST(lambda a0,a1,a2,a3 : (1 if a0=='n' else 0 )+ (1 if a1=='y' else 0 )+ (1 if a2=='n' else 0 )+ (1 if a3=='n' else 0 ) >= 3)
    ) 
    def r0(self):
        print("You are doing okay")
        print("You can keep doing what you are doing")
        print("If you have any problem, you can always try toseek help from people close to you")
        exit()
        
init(autoreset=True)
es = MentalHealthConsultant()
es.reset()
es.run()