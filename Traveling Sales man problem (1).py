#!/usr/bin/env python
# coding: utf-8

# # Traveling Sales Man Problem
# 
# ### To Do
# <ul>
#     <li>Generalize the Chromosome values searching part i.e. in the fitness function </li>
# </ul>
# 

# ## Table of Contents
# <ol style='font-size:12pt;font-weight:bold;|'>
#     <li><a style='text-decoration:none;' href='#1'>Definition of the Fitness Function</a></li>
#     <li><a style='text-decoration:none;' href='#2'>Fitness Evaluation Function</a></li>
#     <li><a style='text-decoration:none;' href='#3'>Initializing the Population</a></li>
#     <li><a style='text-decoration:none;' href='#4'>Fitness Evaluation</a></li>
#     <li><a style='text-decoration:none;' href='#5'>Selection</a></li>
#     <li><a style='text-decoration:none;' href='#6'>CrossOver</a></li>
#     <li><a style='text-decoration:none;' href='#7'>Conversion To Ordinal Representation</a></li>
#     <li><a style='text-decoration:none;' href='#8'>Conversion of Chromosomes back to their Original form</a></li>
#     <li><a style='text-decoration:none;' href='#9'>CrossOver Function</a></li>
#     <li><a style='text-decoration:none;' href='#10'>Mutation</a></li>
#     <li><a style='text-decoration:none;' href='#11'>The Main Algorithm</a></li>
#                                                                                
# </ol>

# <h2>1. Definition of the Fitness function<a href='#' id='1'></a></h2>
# 

# In[1]:


import numpy as np
c1=(1,1)
c2=(2,4)
c3=(4,2)
c4=(4,5)
c5=(2,6)
c6=(5,4)
c7=(5,6)
c8=(2,1,)
c9=(9,11,)
c10=(10,11)
c11=(6,8)
c12=(12,11)
c13=(13,15)
c14=(15,13)
c15=(16,18)
c16=(18,16)
c17=(20,21)
c18=(21,20)
c19=(18,24,)
c20=(24,18)
c21=(22,23)
c22=(23,22)
c23=(27,25)
c24=(25,27)
c25=(29,32)
c26=(32,35)



def ChromosomeValues(chromosome1,chromosome2,CityDict):
    
    for ky in CityDict.keys():
        if(ky==chromosome1):
            x1,y1=CityDict[ky]
            break
    for ky in CityDict.keys():
        if(ky==chromosome2):
            x2,y2=CityDict[ky]
            break
    """"if(chromosome1=="c1"):
            x1,y1=c1
    elif (chromosome1=="c2"):
        x1,y1=c2
    elif (chromosome1=="c3"):
        x1,y1=c3
    elif (chromosome1=="c4"):
        x1,y1=c4
    elif (chromosome1=="c5"):
        x1,y1=c5
    elif (chromosome1=="c6"):
        x1,y1=c6
        
    elif (chromosome1=="c7"):
        x1,y1=c7
    
    elif (chromosome1=="c8"):
        x1,y1=c8
    elif (chromosome1=="c9"):
        x1,y1=c9
    elif (chromosome1=="c10"):
        x1,y1=c10
    elif (chromosome1=="c11"):
        x1,y1=c11
    elif (chromosome1=="c12"):
        x1,y1=c12
    elif (chromosome1=="c13"):
        x1,y1=c13
    elif (chromosome1=="c14"):
        x1,y1=c14
    elif (chromosome1=="c15"):
        x1,y1=c15
    elif (chromosome1=="c16"):
        x1,y1=c16
    elif (chromosome1=="c17"):
        x1,y1=c17
    elif (chromosome1=="c18"):
        x1,y1=c18
    elif (chromosome1=="c19"):
        x1,y1=c19
    elif (chromosome1=="c20"):
        x1,y1=c20
    elif (chromosome1=="c21"):
        x1,y1=c21
    elif (chromosome1=="c22"):
        x1,y1=c22
    elif (chromosome1=="c23"):
        x1,y1=c23
    elif (chromosome1=="c24"):
        x1,y1=c24
    elif (chromosome1=="c25"):
        x1,y1=c25
        
    if(chromosome2=="c1"):
        x2,y2=c1
    elif (chromosome2=="c2"):
        x2,y2=c2
    elif (chromosome2=="c3"):
        x2,y2=c3
    elif (chromosome2=="c4"):
        x2,y2=c4
    elif (chromosome2=="c5"):
        x2,y2=c5
    elif (chromosome2=="c6"):
        x2,y2=c6
        
    elif (chromosome2=="c7"):
        x2,y2=c7
    
    elif (chromosome2=="c8"):
        x2,y2=c8
    elif (chromosome2=="c9"):
        x2,y2=c9
    elif (chromosome2=="c10"):
        x2,y2=c10
    elif (chromosome2=="c11"):
        x2,y2=c11
    elif (chromosome2=="c12"):
        x2,y2=c12
    elif (chromosome2=="c13"):
        x2,y2=c13
    elif (chromosome2=="c14"):
        x2,y2=c14
    elif (chromosome2=="c15"):
        x2,y2=c15
    elif (chromosome2=="c16"):
        x2,y2=c16
    elif (chromosome2=="c17"):
        x2,y2=c17
    elif (chromosome2=="c18"):
        x2,y2=c18
    elif (chromosome2=="c19"):
        x2,y2=c19
    elif (chromosome2=="c20"):
        x2,y2=c20
    elif (chromosome2=="c21"):
        x2,y2=c21
    elif (chromosome2=="c22"):
        x2,y2=c22
    elif (chromosome2=="c23"):
        x2,y2=c23
    elif (chromosome2=="c24"):
        x2,y2=c24
    elif (chromosome2=="c25"):
        x2,y2=c25"""
    #print(x1,y1,x2,y2) 
    return (x1,y1,x2,y2)
    
    
def Dist(AChromosome):
    CitiesList=[(1,1),(2,4),(4,2),(4,5),(2,6),(5,4),(5,6),(2,1,),(9,11,),
            (10,11),(6,8),(12,11),(13,15),(15,13),(16,18),(18,16),(20,21),(21,20),
            (18,24,),(24,18),(22,23),(23,22),(27,25),(25,27),(29,32),(32,35)]
    CitiesDict={}
    for i in range(len(CitiesList)):
        CitiesDict[(('c'+str(i+1)))]=CitiesList[i]
    
    distance=0
    x=0
    #print(AChromosome)
    y=0     
    for i in range(0,len(AChromosome)-1):
        x1,y1,x2,y2=ChromosomeValues(AChromosome[i],AChromosome[i+1],CitiesDict)
        num=float(np.sqrt(((x2-x1)**2+(y2-y1)**2)))
        distance=distance+num
    
    return distance


# <h2><a href='#' id='2'></a> 2. Fitness Evaluation Function</h2>
# 
# 
# 
# 

# In[2]:


def FitnessEval(Chromosome):
    Fitness= [Dist(Chromosome[i]) for i in range(len(Chromosome))]
    #Fitness=Dist(Chromosome[0])
    return Fitness


# <h2><a href='#' id='3'></a> 3. Initializing the population</h2>
# <p>Randomly placing the cities inside chromosomes</p>

# In[3]:


totalCities=25
cities=["c"+str(i+1) for i in range(totalCities)]
cities=np.array(cities)
#cities


# In[4]:



def Initialization():
    chromosome=[]
    for i in range(totalCities):
        while(len(chromosome)!=totalCities):
            city="c"+str(np.random.randint(1,26))
            if(city in chromosome):
                continue
            else:
                chromosome.append(city)
                
    return chromosome

# Setting size of population to be 20
Chromosome=[]
for i in range(20):
    Chromosome.append(Initialization())

#Chromosome
    


# <h2><a href='#' id='4'></a> 4. Fitness Evaluation</h2>
# <p>We have to evaluate the fitness of each chromosome and will store the fitness score in a separate array</p>

# In[5]:


Fitness1= FitnessEval(Chromosome)
#Fitness=Dist(Chromosome[0])
#Fitness1


# In[ ]:





# <h2><a href='#' id='5'></a> 5. Selection</h2>
# <p>The chromosome with the smallest distance would be allowed to go into further steps i.e crossover and mutation.<br>
#     The 50% of the total population (<strong>10 Individuals</strong>) will be selected who have the smallest distance.
# <p>

# In[6]:


def Selection():
    # Convert the logic from max value selection to min value selection
    dict_key=[str(i+1) for i in range(20)]
    
    Chromosome_Fitness={dict_key[i]:Fitness1[i] for i in range(20)}
    #Chromosome_Fitness
    keep=[]
    
    lst=[float(Chromosome_Fitness[i]) for i in Chromosome_Fitness.keys()]
    lst=np.array(lst)
    for i in range(10):
        x=max(lst)
        for j in range(20):
            if Chromosome_Fitness[str(j+1)]==x:
                lst[j]=None
                Chromosome_Fitness[str(j+1)]=""
                break


    #print(keep1)
    keep=[]
    keep_fitness=[]
    for val in Chromosome_Fitness:
        if Chromosome_Fitness[val]!="":
            keep.append(str(int(val)-1))
            keep_fitness.append(Chromosome_Fitness[val])
    #print(keep)


    #Selection of chromosomes and copying the chromosomes into new chromosomes
    NewChromosome=[]
    for i in range(10):
        NewChromosome.append(Chromosome[(int(keep[i]))])

    return NewChromosome


# <h2><a href='#' id='6'></a> 6. CrossOver</h2>
# <p>The chromosomes with the index numbers that are stored in the "keep" are crossovered to produce new offsprings.<br>
# The crossover rate would be 0.4 which means:<br>
#        number of crossover points = total no of genes * 0.4<br>
#        number of crossover points = 250 * 0.4 = 100 crossover points
#     <br>
#     <strong>But!</strong>
#     <br>
#     as we have we are going to perform ordinal crossover for the reason to avoid the duplication in the cities while performing crossover, we will first convert the selected chromosomes into their ordinal representation. And for this reason we have use the " ConvertToOrdinal "
# 
# </p>

# <h2><a href='#' id='7'></a> 7. Conversion to Ordinal Representation</h2>

# In[7]:


def ConvertToOrdinal(Chr):
    arr=['c'+str(k+1) for k in range(len(Chr))]
    OrdinalArr=np.arange(0,25)
    #print(arr)
    for x in range(len(Chr)):
        #Searching the chromosome
        for i in range(0,len(Chr)):
            if (Chr[x]==arr[i]):
                OrdinalArr[x]=i+1
                for j in range(i,((len(arr)-1))):
                    arr[j]=arr[j+1]
                    arr[j+1]=None
                break
    #print(Chr)
    #print(OrdinalArr) 
    return OrdinalArr


# <h2><a href='#' id='8'></a> 8. Conversion of Chromosomes back to their original form</h2>

# In[8]:


def ConverToOriginal1(Chr):
    OriginalChr=['c'+str(i+1) for i in range(len(Chr))]
    arr=[i+1 for i in range(len(Chr))]
    OriginalRep=[]
    #print(OriginalChr)
    #print(Chr)
    #Conversion
    for i in range(len(Chr)):
        ind=Chr[i]
        ind=ind-1
        org=OriginalChr[ind]
        OriginalRep.append(org)
        #print(OriginalRep)
        for j in range(ind,len(OriginalChr)-1):
            #print(OriginalChr)
            OriginalChr[j]=OriginalChr[j+1]
            OriginalChr[j+1]=None
        OriginalChr[(len(Chr)-1)]=None
    
    return OriginalRep


def ConvertToOriginal(chromosome):
    OriginalChromosome=[]
    for i in range(len(chromosome)):
        result=ConverToOriginal1(chromosome[i])
        OriginalChromosome.append(result)
    
    return OriginalChromosome


# <h2><a href='#' id='9'></a> 9. CrossOver Function</h2>

# In[9]:


#Perform Crossover and try to solve the problem occuring repeatedly (Index out of bound)
def crossover(chromosome):
    OrdinalRep=[]
    CrossOverRate=0.3
    CrossOverPoints=int(((len(chromosome)*len(chromosome[0]))*CrossOverRate))
    for i in range(len(chromosome)):
        result=ConvertToOrdinal(chromosome[i])
        OrdinalRep.append(result)
    
    #print("Before Crossover")
    #print(OrdinalRep)
    
    #Performing CrossOver
    count=0
    for pt in range(1,CrossOverPoints+1):
        count+=1
        Chrm1=np.random.randint(0,(len(OrdinalRep)))
        #Chrm1=OrdinalRep[Chrm1]
        while(True):    
            Chrm2=np.random.randint(0,(len(OrdinalRep)))
            #Chrm2=chromosome[Chrm2]
            if(Chrm1==Chrm2):
                Chrm2=np.random.randint(0,(len(OrdinalRep)))
                #Chrm2=chromosome[Chrm2]
            else:
                break
        #print(f"Chrm1= {Chrm1} and Chrm2= {Chrm2}")
        Cpoint=np.random.randint(1,(len(OrdinalRep[0])))
        temp=0
        for i in range(len(OrdinalRep[Chrm1])):
            if (i==Cpoint):
                for j in range(i,len(OrdinalRep[Chrm1])):
                    temp=OrdinalRep[Chrm1][j]
                    OrdinalRep[Chrm1][j]=OrdinalRep[Chrm2][j]
                    OrdinalRep[Chrm2][j]=temp
                break
                
    #print(f"No of Crossovers: {count}")
    return OrdinalRep


# ##### <h2><a href='#' id='10'></a> 10. Mutation</h2>
# <p>
#     Now we have to perform mutation in order to avoid stuking in local optima.<br>
#     We have set the mutation rate = 0.05, which means:
#     <br>number of mutation points= total no of genes * 0.05
#     <br>number of mutation points= 250 * 0.05= 12.5 = 13 approx <br>
#     <strong>Note That!</strong>
#     <br> we will perform on the ordinally represented chromosomes
#     
# </p>

# In[10]:


def Mutation(Chr):
    mutRate=0.05
    mutPoint=int(np.ceil(((len(Chr[0]))*(len(Chr)))*(mutRate)))
    while(mutPoint!=0):
        ranChromIndex=np.random.randint(0,len(Chr))
        ranChromMutPoint1=np.random.randint(0,len(Chr[ranChromIndex]))
        ranChromMutPoint2=np.random.randint(0,len(Chr[ranChromIndex]))
        if(ranChromMutPoint1==ranChromMutPoint2):
            while(True):
                ranChromMutPoint2=np.random.randint(0,len(Chr[ranChromIndex]))
                if(ranChromMutPoint1!=ranChromMutPoint2):
                    break
                
                else:
                    continue
                    
        #Specialized Mutation        
        randVal=Chr[ranChromIndex][ranChromMutPoint1]
        Chr[ranChromIndex][ranChromMutPoint1]=Chr[ranChromIndex][ranChromMutPoint2]
        Chr[ranChromIndex][ranChromMutPoint2]=randVal
        
        mutPoint=mutPoint-1
        
    return Chr
    


# In[11]:


for i in range(20):
    print(f"{i}: {Fitness1[i]}")
Chromosomexy=Selection()
Chromosomexy=crossover(Chromosomexy)
#Chromosomexy


# In[12]:


xy=ConvertToOriginal(Chromosomexy)
#xy


# ## Fitness Evaluation

# In[13]:


Fitness=FitnessEval(xy)
Fitness


# In[14]:


min(Fitness)


# <h2><a href='#' id='11'></a> 11. The Main Algorithm</h2>

# In[21]:


maxIterations=int(100*(len(xy[0])))
ky=''
val=0.0
Results={}
for i in range(2500):
    
    Chromosome1=Selection()
    Chromosome2=Chromosome1
    Chromosome2=crossover(Chromosome2)
    Chromosome1=ConvertToOriginal(Chromosome2)
    Chromosome1=Mutation(Chromosome1)
    FitnessA=list((FitnessEval(Chromosome1)))
    for i in range(len(Chromosome1)):
        ky=''
        val=FitnessA[i]
        for j in Chromosome1[i]:

            ky+=j

        Results[ky]=val


# In[22]:


#Results


# In[23]:


min(Results.values())


# In[24]:


min(Results)


# In[25]:


import matplotlib.pyplot as plt


# In[26]:


fig=plt.figure(figsize=(200,8))
ax=fig.add_axes([0,0,1,1])
y=list(Results.values())
x=np.arange(1.0,((len(Results.values()))+1))

ax.plot(x,y,ls='--',lw=0.5,color='blue',marker='o',markerfacecolor='red',markeredgecolor='red')


# In[ ]:




