import os,re,glob,commands
class Sample(object):
    """A sample is an object containing all the read information of a sample"""
     
    def __init__(self, name):
        """Create a new sample"""
        self.name = name

    def getName(self):
        return self.name
    
    def setRawReads(self, r):
        self.rawReads = r
        
    def getRawReads(self):
        return self.rawReads
    
    def setTrimmedReads(self, t):
        self.trimmedReads = t
        
    def getTrimmedReads(self):
        return self.trimmedReads
    
    def setMatchedReads(self, m):
        self.matchedReads = m
        
    def getMatchedReads(self):
        return self.matchedReads
    
    def setPairedAligned(self, p):
        self.pairedAligned = p
        
    def getPairedAligned(self):
        return self.pairedAligned
    
    def setSingleAligned(self, s):
        self.singleAligned = s
        
    def getSingleAligned(self):
        return self.singleAligned
    
    def __str__(self):
        return self.name + ',' + str(self.rawReads) + ',' + str(self.trimmedReads) + ',' + str(self.matchedReads) + ',' + str(self.pairedAligned) + ',' + str(self.singleAligned)

sampleList=[]
listOfFiles = glob.glob('*.gz')
print listOfFiles
SampleID = list(listOfFiles)
i=0
for item in listOfFiles:
    SampleID[i] = re.split('\.|_', str(item))[0]
    i = i + 1
prefixSet=list(set(SampleID))
prefixSet.sort()
print prefixSet
x = 0

for prefix in prefixSet:
    x = Sample(prefix)
    sampleList.append(x)
    result1 = commands.getoutput('zcat '+ prefix + '_1.fq.gz | wc -l')
    numreads = result1
    print result1
    #result2 = commands.getoutput('zcat ' + prefix + '_2.fq.gz | wc -l')
    #numreads = numreads + int(result2)/4.0
    #x.setRawReads(numreads)
    #x=x+1


    
sample1 = Sample('Gv10-H-06')
sample1.setRawReads(1000)
sample1.setTrimmedReads(2000)
sample1.setMatchedReads(52412)
sample1.setPairedAligned(428236)
sample1.setSingleAligned(74293)
print sample1