import sys, os
from ROOT import TChain, TFile, TTree
from time import time

def select_file(inputdir, outputdir):
  suffix = ["15md", "15mu", "16md", "16mu", "17md", "17mu", "18md", "18mu"]
  prefix = "Tuple_Bp_"
  for suf in suffix:
    inputfile = inputdir + prefix + suf + ".root"
    outputfile = outputdir + "output_cut_data_" + suf + ".root"
    cut_TRUEID(inputfile, outputfile)

def cut_TRUEID(inputfile, outputfile):
  outputfile = TFile(outputfile, "recreate")
  ch = TChain("DecayTree")
  ch.Add(inputfile)
  ID_cut = "mum1_PT>500 && mup1_PT>500 && mum2_PT>500 && mup2_PT>500 && mum1_TRACK_CHI2NDOF<3 && mup1_TRACK_CHI2NDOF<3 && mum1_ProbNNmu>0.2 && mup1_ProbNNmu>0.2 && mum2_ProbNNmu>0.2 && mup2_ProbNNmu>0.2 && mum1_TRACK_GhostProb<0.47 && mup1_TRACK_GhostProb<0.47 && mum1_PIDmu>0 && mup1_PIDmu>0 && mum2_PIDmu>0 && mup2_PIDmu>0 && Jpsi_M>3040 && Jpsi_M<3194  && Kp_ProbNNk>0.2 && Bp_IPCHI2_OWNPV<25 && Bp_ENDVERTEX_CHI2 / Bp_ENDVERTEX_NDOF < 10"
  mytree = ch.CopyTree(ID_cut)
  mytree.Write()
  outputfile.Close()

if __name__ == "__main__":
  start = time()
  path = "/nishome/menghan/disk402/JpsiMuMuK"
  select_file(path + "/raw/", path + "/after_cut/")
  end = time()
  print("All jobs done")
  print(str(end - start) + "s")
