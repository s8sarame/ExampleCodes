from NaiveBayes import NaiveBayes
import numpy as np
import math
b = NaiveBayes("training2.tsv")
class test1:
    def __init__(self, filename):
        prior_prob = b.prior
        j = 0
        with open(filename, 'r') as obj:
            m = 0
            c, tp, tn, fp, fn, probability = 0, 0, 0, 0, 0, 0
            for line in obj:
                line = [int(element) for element in line.split('\t')]
                original=line[0]
                
                for i in range(1, len(line)):
                    Numerator = b.feat_1[i-1][line[i]]
                    Denominator = b.feat_0[i-1][line[i]]
                    c += (Numerator - Denominator)
                    probability = prior_prob + c
                if probability > 0:
                    predicted = 1
                else:
                    predicted = 0
                if original == 1 and predicted == 0:
                    fp += 1
                if original == 1 and predicted == 1:
                    tp += 1
                if original == 0 and predicted == 1:
                    fn += 1
                if original == 0 and predicted == 0:
                    tn += 1
                    
                j += 1
                print(j," ",(probability))

        total = (tp + tn + fp + fn)
        accuracy = ((tp + tn)/total)
        print('Accuracy: ', accuracy)
                    
t = test1("test2.tsv")
