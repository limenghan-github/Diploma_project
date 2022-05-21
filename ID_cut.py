import sys, os
from ROOT import TChain, TFile, TTree
from time import time

def select_file(inputdir, outputdir):
  suffix = ["16md", "16mu"]
  prefix = "Bp_"
  for suf in suffix:
    inputfile = inputdir + "Tuple_" + prefix + suf + ".root"
    outputfile = outputdir + "ID_cut_MC_" + prefix + suf + ".root"
    cut_TRUEID(inputfile, outputfile, prefix)

def cut_TRUEID(inputfile, outputfile, prefix):
  outputfile = TFile(outputfile, "recreate")
  ch = TChain("DecayTree")
  ch.Add(inputfile)
  ID_cut_Bp = "abs(mup1_TRUEID) == 13 && abs (Kp_TRUEID) == 321 && abs(mum1_TRUEID) == 13 && abs(mup2_TRUEID) == 13 && abs(mum2_TRUEID) == 13 && abs(Jpsi_TRUEID) == 443 && abs(Kp_MC_MOTHER_ID) == 521 && abs(Jpsi_MC_MOTHER_ID)==9920443 && abs(mup1_MC_MOTHER_ID) == 443 && abs(mum1_MC_MOTHER_ID) == 443 && abs(mup2_MC_MOTHER_ID) == 9920443 && abs(mum2_MC_MOTHER_ID) == 9920443 && mum1_PT>250 && mup1_PT>250 && mum2_PT>250 && mup2_PT>250 && mum1_TRACK_CHI2NDOF<3 && mup1_TRACK_CHI2NDOF<3 && mum1_ProbNNmu>0.2 && mup1_ProbNNmu>0.2 && mum2_ProbNNmu>0.2 && mup2_ProbNNmu>0.2 && mum1_TRACK_GhostProb<0.47 && mup1_TRACK_GhostProb<0.47 && mum1_PIDmu>0 && mup1_PIDmu>0 && mum2_PIDmu>0 && mup2_PIDmu>0 && Jpsi_M>3040 && Jpsi_M<3194  && Kp_ProbNNk>0.2 && Bp_IPCHI2_OWNPV<25 && Bp_ENDVERTEX_CHI2 / Bp_ENDVERTEX_NDOF < 10"
  mytree = ch.CopyTree(ID_cut_Bp)
  mytree.Write()
  outputfile.Close()

if __name__ == "__main__":
  start = time()
  path = "/nishome/menghan/disk402/JpsiMuMuK/MC"
  select_file(path + "/raw/", path + "/mc_cut/")
  end = time()
  print("All jobs done")
  print(str(end - start) + "s")
