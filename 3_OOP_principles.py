#!/usr/bin/python3

class Person():
    ''' Person class '''

    def __init__(self, name='Noname', age=0, gender='None', sexuality='None', religion='None'):
        '''Initialize person'''
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__sexuality = sexuality
        self.__religion = religion

    def get_name(self):
        '''Return person name'''
        return self.__name
  
    def set_name(self, name):
        '''Set person age'''
        self.__name = name
        return self.__name

    def get_age(self):
        '''Return person age'''
        return self.__age

    def set_age(self, n):
        '''Set person age'''
        self.__age = n
        return self.__age

    def get_gender(self):
        '''Return person gender'''
        return self.__gender

    def set_gen(self, gen):
        '''Set person age'''
        self.__gender = gen
        return self.__gender

    def get_sexuality(self):
        '''Return person sexuality'''
        return self.__sexuality
     
    def set_sex(self, sex):
        '''Set person sexuality'''
        self.__sexuality = sex
        return self.__sexuality

    def get_religion(self):
        '''Return person religion'''
        return self.__religion
   
    def set_rel(self, rel):
        '''Set person rel'''
        self.__religion = rel
        return self.__religion

class Teacher(Person):
    '''Teacher class inherits from Person class'''

    def __init__(self, knowledge, experience):
        '''Ininitializing teacher'''
        super().__init__()
        self.__knowledge = knowledge
        self.__experience = experience

    def get_knowledge(self):
        '''Return teacher knowledge'''
        return self.__knowledge

    def set_knowledge(self, know):
        '''Set teacher knowledge'''
        self.__knowledge = know
        return self.__knowledge
        
    def get_experience(self):
        '''Return teacher experience'''
        return self.__experience

    def set_experience(self, exp):
        '''Set teacher experience'''
        self.__experience = exp
        return self.__experience

    def get_religion(self):
        '''
        Return teacher religion
        if he/she wants to
        '''

        print('Do you want to share this?')
        answer = input()

        if answer == 'yes':
            print('Thank you for your consent')
            return (super().get_religion())
 
        if answer == 'no':
            print('Sorry person doesnt want to share religion')
            return

        else:
            print('Answer needs to be yes or no')
            return

man = Person('sech', 34, 'Male', 'Hetero', 'Christian')
print('Person religion is: ', man.get_religion())

Teacher_1 = Teacher('Math', 4)
Teacher_1.set_rel('Catolic')
print('Teacher Religion is: ', Teacher_1.get_religion())
