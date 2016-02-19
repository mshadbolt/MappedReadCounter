import os,re,glob


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

for prefix in prefixSet:
    unzip1 = 'gunzip -d -c -f -k '+ prefix + '*paired* > ' + prefix + '.paired.bowtie'
    unzip2 = 'gunzip -d -c -f -k '+ prefix + '*_1*.singles* > ' + prefix + '_1.singles.bowtie'
    unzip3 = 'gunzip -d -c -f -k '+ prefix + '*_2*.singles* > ' + prefix + '_2.singles.bowtie'
    catcmd = 'cat ' + prefix + '.paired.bowtie ' + prefix + '_1.singles.bowtie ' + prefix + '_2.singles.bowtie > ' + prefix + '.bowtie' 
    zipcmd = 'gzip -f -c -9 ' + prefix + '.bowtie > ' + prefix + '.bowtie.gz'    
    rmcmd = 'rm ' + prefix + "*.bowtie"
    mvcmd = 'mv ' + prefix + '.bowtie.gz Merged'
    os.system(unzip1)
    os.system(unzip2)
    os.system(unzip3)
    os.system(catcmd)
    os.system(zipcmd)
    os.system(rmcmd)
    os.system(mvcmd)