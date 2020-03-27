from random import randint, choice, shuffle
import itertools


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = self.generateNewValue(problParam['max'])
        self.__fitness = 0

    def generateNewValue(self, max):
        permutation=[]
        for i in range(1,max):
            permutation.append(i)
        shuffle(permutation)
        permutation.insert(0,0)
        return permutation

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0):
        self.__fitness = fit

    def crossover(self, c):
        pos1 = randint(1, len(self.__repres) - 1)
        pos2 = randint(1, len(self.__repres) - 1)
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1

        newrepres = self.__repres[pos1:pos2]
        whereToAdd = 0

        for elem in c.repres:
            if elem not in newrepres:
                if whereToAdd < pos1:
                    newrepres.insert(whereToAdd, elem)
                    whereToAdd += 1
                else:
                    newrepres.append(elem)
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        pos1 = randint(1, len(self.__repres) - 1)
        pos2 = randint(1, len(self.__repres) - 1)
        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

# c=Chromosome()
# print(c.generateNewValue(10))