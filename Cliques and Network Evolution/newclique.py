from collections import defaultdict
import random
import copy
import tools

class calculate_cliques:
    def __init__(self, filename):
        self.network = defaultdict(set)
        self.edges = set()
        with open(filename, 'r')as obj:
            for data in obj:
                data = data.split()
                self.edges.add(tuple(sorted([data[0],data[1]])))
                self.network[data[0]].add((data[1]))

    def cliques(self):
       #calculate cliques of 3
        three = set()
        for v in self.edges:
            for j in self.edges:
                if v[0]==j[0] and (v[1],j[1]) in self.edges:
                    three.add(tuple(sorted([v[0],v[1],j[1]])))
        #calculate cliques of 4
        four = set()
        for node1,node2,node3 in three:
            for node4,vals in self.network.items():
                if  {node1,node2,node3}.issubset(vals):
                    four.add(tuple(sorted([node1,node2,node3,node4])))
        
        #calculate cliques of 5
        five = set()
        for node1,node2,node3,node4 in four:
            for node5,val in self.network.items():
                if {node1,node2,node3,node4}.issubset(val):
                    five.add(tuple(sorted([node1,node2,node3,node4,node5])))
                  
        self.final_5 = len(five)
        
        #remove cliques of 4 which are already present in 5
        duplicate_in_4 = set()
        for node1,node2,node3,node4 in four:
            for nodes_of_5 in five:
                if {node1,node2,node3,node4}.issubset(nodes_of_5):
                    duplicate_in_4.add(tuple(sorted([node1,node2,node3,node4])))
        self.final_4 = len(four.difference(duplicate_in_4))
        
        #remove cliques of 3 which are already present in 4
        duplicate_in_3 = set()
        for node1,node2,node3 in three:
            for nodes_of_4 in four:
                if {node1,node2,node3}.issubset(nodes_of_4):
                    duplicate_in_3.add(tuple(sorted([node1,node2,node3])))
        self.final_3 = len(three.difference(duplicate_in_3))
       
        return self.final_3,self.final_4,self.final_5
   
    def evolving_networks(self,t):
        for time in range(0,t):
            j = random.random()
            if j < 0.5 or not self.edges:
                while True:
                    n1,n2 = random.sample(self.network.keys(),2)
                    if tuple(sorted({n1,n2})) not in self.edges:
                        break
                    self.network[n1].add(n2)
                    self.network[n2].add(n1)
                    self.edges.add((n1,n2))
            else:
                n1,n2 = random.choice(list(self.edges))
                self.network[n1].discard(n2)
                self.network[n2].discard(n1)
                self.edges.discard((n1,n2))

    def randomising_network(self):
        new_network = copy.deepcopy(self)
        m = len(new_network.edges)
        for ite in range(0,2*m):
            while(True):
                e1, e2 = random.choice(list(new_network.edges))
                e3, e4 = random.choice(list(new_network.edges))
                if e1 != e4 and e3 !=e2:
                    break
                new_network.edges.add(tuple(sorted([e1, e4])))
                new_network.edges.add(tuple(sorted([e3,e2])))
                new_network.network[e1].discard(e2)
                new_network.network[e2].discard(e1)
                new_network.network[e1].add(e4)
                new_network.network[e4].add(e1)
                new_network.network[e3].discard(e4)
                new_network.network[e4].discard(e3)
                new_network.network[e3].add(e2)
                new_network.network[e2].add(e3)
        return new_network
           
    def motif(self,n):
        network_m = calculate_cliques("rat_network.tsv")
        c_orginal_3,c_orginal_4,c_orginal_5 = network_m.cliques()
        c_3 = []
        c_4 = []
        c_5 = []
        for i in range(n):
            rand_net = network_m.randomising_network()
            tem1,tem2,tem3 = rand_net.cliques()
            c_3.append(tem1)
            c_4.append(tem2)
            c_5.append(tem3)
        c3c=0
        c4c=0
        c5c=0
        for c3 in c_3:
            if c3>=c_orginal_3:
                c3c+=1
        for c4 in c_4:
            if c4>=c_orginal_4:
                c4c+=1
        for c5 in c_5:
            if c5>=c_orginal_5:
                c4c+=1
        print(c3c,c4c,c5c)
        p3 = c3c/n
        p4 = c4c/n
        p5 = c5c/n
        print(p3,p4,p5)
      
def cie():
    network1 = calculate_cliques("rat_network.tsv")
    c13 = []
    c14 = []
    c15 = []
    temp1, temp2, temp3 = network1.cliques()
    c13.append(temp1)
    c14.append(temp2)
    c15.append(temp3)
    print(c13,c14,c15)
    for i in range(100):
        network1.evolving_networks(1)
        temp1, temp2, temp3 = network1.cliques()
        c13.append(temp1)
        c14.append(temp2)
        c15.append(temp3)
    
    tools.plot_cliques([c13], "Clique 3", "graph of cliques")
    tools.plot_cliques([c14], "Clique 4", "graph of cliques")
    tools.plot_cliques([c15], "Clique 5", "graph of cliques")
    
    for j in range(900):
        network1.evolving_networks(1)
        temp1, temp2, temp3 = network1.cliques()
        c13.append(temp1)
        c14.append(temp2)
        c15.append(temp3)
    print(c13,c14,c15)

a = calculate_cliques("rat_network.tsv")
a.__init__("rat_network.tsv")
a.cliques() 
a.randomising_network()
a.evolving_networks()
a.motif(100)
a.cie()