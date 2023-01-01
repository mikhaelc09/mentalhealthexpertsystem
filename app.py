from experta import *

class SleepingQuality(Fact):
    # a4, b4, b5, b7
    pass

class EatingHabit(Fact):
    # a2, b2
    pass

class ExerciseRoutine(Fact):
    # a3, b3
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
        print(es.facts)

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
        print(es.facts)

    @Rule(AS.f << State(action='interviewing', number=3))
    def a3(self, f):
        while(True):
            x = input('Do you exercise regularly? [y/n] : ').lower()
            if(x == 'y' or x == 'n'):
                break
            print("Please enter a valid answer")
        self.retract(f)
        self.declare(State(action='interviewing', number=4))
        self.declare(ExerciseRoutine(regular=x))
        print(es.facts)

    # Conlusion -> Example
    @Rule(AND(EatingHabit(well='n'), MindCondition(down='y')))
    def r1(self):
        print("You are depressed!")
    

    @Rule() # No rules for else condition
    def r0(self):
        print("You are okay")

es = MentalHealthConsultant()
es.reset()
es.run()