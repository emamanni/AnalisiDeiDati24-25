'''
computeMedian() computes the median of a sample
input: a list of number called "sample"
output: the median of the sample
'''
def computeMedian (sample):
    sample.sort()
    if len(sample) % 2 == 0: # the length of sample is even !!!
        return (sample[len(sample)//2 - 1] + sample[len(sample)//2])/2
    else: # the length of sample is odd !!!
        return sample[(len(sample)+1) // 2 - 1] 
    
