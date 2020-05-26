import numpy as np
from collections import Counter
from operator import itemgetter
from itertools import chain
class NaiveBayes:

    def __init__(self, filename):
        data = []
        with open(filename, 'r') as obj:
            for line in obj:
                line= [int(element) for element in line.split('\t')]
                data.append(np.asarray(line))

        num_features = 100
        x = [data[i][0:num_features+1] for i in range (0, len(data))]
        y = [int (data[i][0]) for i in range (0, len(data))]
        count_y = []
        #counting number of 0s and 1s
        count_y = Counter(y) 
        #Calculating prior probabilities of class 0 and 1
        x_list_0 = [x[i] for i in range (len(x)) if y[i]==0]
        x_list_1 = [x[i] for i in range(len(x))if y[i]==1]
        No_Complex_data=[ [] for i in range(len(x_list_0[0])-1) ]
        Complex_data=[ [] for i in range(len(x_list_1[0])-1) ]
          #print(len(No_Complex_data))
        for i in range(0,len(x_list_0)):
            for j in range(1,len(x_list_0[i])):
                No_Complex_data[j-1].append(x_list_0[i][j])
                  
        for i in range(0,len(x_list_1)):
            for j in range(1,len(x_list_1[i])):
                Complex_data[j-1].append(x_list_1[i][j])
                
        self.feat_0=[ [] for i in range(len(No_Complex_data)) ]
        self.feat_1=[ [] for i in range(len(Complex_data) )]
       
        #log likelihood of features for class 0
        for i in range(0, len(No_Complex_data)):
            self.feat_0[i]=(Counter(No_Complex_data[i]))
            for j in range(0,len(self.feat_0[i])):
                self.feat_0[i][j] /= (len(No_Complex_data[0]))
                self.feat_0[i][j]=np.log10(self.feat_0[i][j])
             
        #log likelihood of features for class 1
        for i in range(0, len(Complex_data)):
            self.feat_1[i]=(Counter(Complex_data[i]))
            for j in range(0, len(self.feat_1[i])):
                self.feat_1[i][j] /= (len(Complex_data[0]))
                self.feat_1[i][j]=np.log10(self.feat_1[i][j])

        p_c=len(Complex_data[0])/200
        p_c1=len(No_Complex_data[0])/200
        self.prior=np.log10(p_c/p_c1)

        sort_feat_0 = sorted(self.feat_0, key=itemgetter(1))
        sort_feat_1= sorted(self.feat_1,key=itemgetter(1))
        
        for i in range(0,len(sort_feat_0)):
           max_lik_0 = sorted([max(sort_feat_0[i].values())])
           max_lik_1 = sorted([max(sort_feat_1[i].values())])
           t0 =[max_lik_0,max_lik_1]
           top_10 =  list(itertools.chain.from_iterable(t0))
           top_10 = sorted(top_10)
           print(top_10)

a = NaiveBayes("training1.tsv")
