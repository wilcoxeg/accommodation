
import pandas as pd
import csv
import os
import itertools
from sklearn.utils import shuffle

condition_dict = {
  "base":100,
  "conditionals":200,
  "possibility":300,
  "question":400,
  "negation":500
}

def construct_items(filepath):
  df = pd.read_csv(filepath)
  df = df.dropna()
  df = df.applymap(str)

  result = []
  plaintext_result = ""

  for i in range(df.shape[0]):

    trigger = df.iloc[i, 0]
    form = df.iloc[i, 1]

    pos = df.iloc[i, 2]
    pos_plus_trig = df.iloc[i,3]
    pos_minus_trig = df.iloc[i,4]

    neut = df.iloc[i, 5]
    neut_plus_trig = df.iloc[i, 6]
    neut_minus_trig = df.iloc[i, 7]


    pos = '[["target_'+trigger+'_'+form+'_positive",'+str(i+condition_dict[trigger])+'], "RangeForm", {html: construct_dialog("'+pos+'", "'+pos_minus_trig+'", "'+pos_plus_trig+'" )}],' + '\n'
    neg = '[["target_'+trigger+'_'+form+'_neutral",'+str(i+condition_dict[trigger])+'], "RangeForm", {html: construct_dialog("'+neut+'", "'+neut_minus_trig+'", "'+neut_plus_trig+'" )}],' + '\n'
    result.append((pos, neg))

    plaintext_result += "\t".join([trigger, form, "positive, minus", pos + "  " + pos_minus_trig+"\n"])
    plaintext_result += "\t".join([trigger, form, "positive, plus", pos + "  " + pos_plus_trig+"\n"])
    plaintext_result += "\t".join([trigger, form, "neutral, minus", neut + "  " + neut_minus_trig+"\n"])
    plaintext_result += "\t".join([trigger, form, "neutral, plus", neut + "  " + neut_plus_trig+"\n"])

  return (result, plaintext_result)

exp_data_prefix = "../data/"
exp_items = []

for file in os.listdir(exp_data_prefix):
  if(file.endswith(".csv")):
    exp_items.append(construct_items(exp_data_prefix + file))

exp_items_plaintext = list(itertools.chain.from_iterable([x[1] for x in exp_items]))

with open("../data/experimental_items/plaintext_items.txt", "w") as outf:
  outf.writelines(exp_items_plaintext)

# Print out the Ibex Experiments in five different files

exp_items_ibex = [x[0] for x in exp_items]
exp_items_ibex = [shuffle(x, random_state=123) for x in exp_items_ibex]

n_exps = 6
for i in range(n_exps):

  start = int( (i/n_exps) * len(exp_items_ibex[0]) )
  stop = int( ((i+1)/n_exps) * len(exp_items_ibex[0]) )

  this_exp_items = [x[start:stop] for x in exp_items_ibex]
  this_exp_items = list(itertools.chain.from_iterable([x for x in this_exp_items]))
  this_exp_items = "".join([x[0]+x[1] for x in this_exp_items])

  with open("../data/experimental_items/ibex_items_"+str(i)+".txt", "w") as outf:
    outf.writelines(this_exp_items)




