
import pandas as pd
import csv

def construct_item(trigger, condition, item, setup, target):
  return "".join(['[[\"', "target"+"_"+trigger+"_"+condition, '\" , ', str(item), '], \"Message\", {html:\"', setup, '\"}, \"Message\", {html: \"', setup, '<br><br><b>', target, '<b>\"},\"AcceptabilityJudgment\", {s: {html: \" How acceptable was the final sentence (in bold) to you?\" }}],'])
  #return " ".join([trigger, condition, str(item), ":  ", setup, target])

def construct_items(filepath):
  df = pd.read_csv(filepath)
  df = df.applymap(str)
  df = df.dropna()

  result = ""

  for i in range(df.shape[0]):

    trigger = df.iloc[i, 0]
    form = df.iloc[i, 1]

    pos = df.iloc[i, 2]
    pos_minus_trig = df.iloc[i,3]
    pos_plus_trig = df.iloc[i,4]

    neut = df.iloc[i, 5]
    neut_minus_trig = df.iloc[i, 6]
    neut_plus_trig = df.iloc[i, 7]


    result += '[["target_'+trigger+'_'+form+'_positive",'+str(i)+'], "RangeForm", {html: construct_dialog("'+pos+'", "'+pos_minus_trig+'", "'+pos_plus_trig+'" )}],' + '\n'
    result += '[["target_'+trigger+'_'+form+'_neutral",'+str(i)+'], "RangeForm", {html: construct_dialog("'+neut+'", "'+neut_minus_trig+'", "'+neut_plus_trig+'" )}],' + '\n'


  return result

items_array = construct_items("./items.csv")

with open("items.txt", "w") as outf:
  outf.writelines(items_array)







