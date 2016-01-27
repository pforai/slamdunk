#!/usr/bin/env python

# Date located in: -
from __future__ import print_function
import os
import subprocess

projectPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
varScanPath = os.path.join(projectPath, "bin", "VarScan.v2.4.1.jar")

def SNPs(inputBAM, outputSNP, referenceFile, minVarFreq, minCov, log, printOnly=False, verbose=True, force=True):
    fileSNP = open(outputSNP, 'w')
    
    mpileupCmd = "samtools mpileup -f" + referenceFile + " " + inputBAM
    if(verbose):
        print(mpileupCmd, file=log)
    if(not printOnly):
        mpileup = subprocess.Popen(mpileupCmd, shell=True, stdout=subprocess.PIPE, stderr=log)
        
    varscanCmd = "java -jar " + varScanPath + " mpileup2snp  --strand-filter 0 --min-var-freq " + str(minVarFreq) + " --min-coverage " + str(minCov) + " --variants 1"
    if(verbose):
        print(varscanCmd, file=log)
    if(not printOnly):
        varscan = subprocess.Popen(varscanCmd, shell=True, stdin=mpileup.stdout, stdout=fileSNP, stderr=log)
        varscan.wait()
    
    fileSNP.close()    