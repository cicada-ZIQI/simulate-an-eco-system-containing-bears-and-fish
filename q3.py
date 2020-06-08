import random

class ecosystem():
    def __init__(self,river_length=13,step=3,n_fish=4,n_bear=2):
        self.length=river_length
        self.step=step
        self.n_fish=n_fish
        self.n_bear=n_bear
        #self.river: a list contains all the bears, fishes and emoty location
        self.river=[]
    
    #randomly allocate fishes and bears into the river before the simulation
    def first_display(self):
        number_of_N=self.length-self.n_bear-self.n_fish
        self.river=["B"]*self.n_bear + ["F"]*self.n_fish + ["N"]*number_of_N
        random.shuffle(self.river)
        print("beginning:",*self.river)
         
    def simulation(self):
        # N represents the number of steps 
        for N in range (1,self.step + 1):
            print("N =",N)
            n=0
            while n < self.length:
                #if the element in the n index is an animal
                if self.river[n] != "N":
                    if n == 0:
                        move=random.randint(0,1)
                    elif n == self.length-1:
                        move=random.randint(-1,0)
                    else:
                        move=random.randint(-1,1)
                    # move towards the left direction
                    if move == -1:
                        # if the elenment in the (n-1)index is none, then just move the animal leftward
                        if self.river[n-1] == "N":
                            self.river[n],self.river[n-1]=self.river[n-1],self.river[n]
                            n += 1
                            print(*self.river)
                        # if the elenment in the (n-1)index is not none and the animal in the n index is a bear
                        elif self.river[n] == "B":
                            # if the elenment in the (n-1)index is also a bear, then a new bear is produced if there are some empty spaces
                            if self.river[n-1] == "B":
                                if "N" not in self.river:
                                        print("No more spaces for a new instance.Over.")
                                        break
                                else:
                                    place=[]
                                    for N in self.river:
                                        if N == "N":
                                            place.append(self.river.index(N))
                                    from random import choice
                                    change=choice(place)
                                    self.river[change]="B"
                                print(*self.river)
                            # if the elenment in the (n-1)index is a fish, then it will be eaten by the bear
                            else:
                                self.river[n]="N"
                                self.river[n-1]="B"
                                print(*self.river)
                            n += 1
                        # if the elenment in the (n-1)index is not none and the animal in the n index is a fish
                        else:
                            # generate a nex fish if there are some spaces
                            if self.river[n-1] == "F":
                                if "N" not in self.river:
                                        print("No more spaces for a new instance.Over.")
                                        break
                                else:
                                    place=[]
                                    for N in self.river:
                                        if N == "N":
                                            place.append(self.river.index(N))
                                    from random import choice
                                    change=choice(place)
                                    self.river[change]="F"
                                    print(*self.river)
                            # the fish will be eaten by the bear leftward
                            else:
                                self.river[n]="N"
                                print(*self.river)
                            n += 1
                    # move rightward
                    elif move == 1:
                        #if the elenment in the (n+1)index is none, then just move the animal righttward
                        if self.river[n+1] == "N":
                            self.river[n],self.river[n+1]=self.river[n+1],self.river[n]
                            print(*self.river)
                            n += 2
                        # if the elenment in the (n+1)index is not none and the animal in the n index is a bear
                        elif self.river[n] == "B":
                            # if the elenment in the (n+1)index is also a bear, then a new bear is produced if there are some empty spaces
                            if self.river[n+1] == "B":
                                if "N" not in self.river:
                                        print("No more spaces for a new instance.Over.")
                                        break
                                else:
                                    place=[]
                                    for N in self.river:
                                        if N == "N":
                                            place.append(self.river.index(N))
                                    from random import choice
                                    change=choice(place)
                                    self.river[change]="B"
                                    print(*self.river)
                            # if the elenment in the (n+1)index is a fish, then it will be eaten by the bear
                            else:
                                self.river[n]="N"
                                self.river[n+1]="B"
                                print(*self.river)
                            n += 1
                        # if the elenment in the (n+1)index is not none and the animal in the n index is a fish
                        else:
                            # if the elenment in the (n+1)index is also a fish, then a new fish is produced if there are some empty spaces
                            if self.river[n+1] == "F":
                                if "N" not in self.river:
                                        print("No more spaces for a new instance.Over.")
                                        break
                                else:
                                    place=[]
                                    for N in self.river:
                                        if N == "N":
                                            place.append(self.river.index(N))
                                    from random import choice
                                    change=choice(place)
                                    self.river[change]="F"
                                    print(*self.river)
                            # the fish will be eaten by the bear rightward 
                            else:
                                self.river[n]="N"
                                print(*self.river)
                            n += 1
                    # if move == 0
                    else:
                        print(*self.river)
                        n += 1
                # if self.river[n] == "N"
                else:
                    n += 1 
            # if no more space for a newly produced instance, than the two loops will both be break      
            else:
                continue
            break 
    
    
a=ecosystem()
a.length=int(input("enter the river length:"))
a.step=int(input("enter the step:"))
a.n_fish=int(input("enter the number of the fish:"))
a.n_bear=int(input("enter the number of the bear:"))
a.first_display()
a.simulation()
 

                            
                            














