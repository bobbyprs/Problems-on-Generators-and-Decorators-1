#Problems on Generators and Decorators
#problem no 2
ll = [input() for _ in range(int(input()))]

def wrapper(fun):
    def phone(ll):
        fun(["+91 "+cn[-10:-5]+" "+cn[-5:] for cn in ll])
    return phone

@wrapper
def sphone(ll):
    print(*sorted(ll), sep='\n')

sphone(ll)
#problem no 1
import operator

people = [input().split() for i in range(int(input()))]
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    
    print(*name_format(people), sep='\n')