class univariate():
    def QuanQual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            #print(columnName) 
            if(dataset[columnName].dtype=='O'):
               #print("qual")
               qual.append(columnName)
            else:
               #print("quan")
               quan.append(columnName)
        return quan,qual   
        
class FREQTABLE(): 
    def freqtable(columnName,dataset):
        freqtable=pd.DataFrame(columns=["Unique_Value","Frequency","Relative_Frequency","Cumsum"])
        freqtable["Unique_Value"]=dataset[columnName].value_counts().index
        freqtable["Frequency"]=dataset[columnName].value_counts().values
        freqtable["Relative_Frequency"]=(freqtable["Frequency"]/103)
        freqtable["Cumsum"]=freqtable["Relative_Frequency"].cumsum()
    return freqtable  

class Central_tedency():    
    def univariate(dataset,quan):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%",
                                "IQR","1.5Rule","Lesser","Greater","min","max"],columns=quan)
    for columnName in quan:
        descriptive.loc["Mean",columnName]=dataset[columnName].mean()
        descriptive.loc["Median",columnName]=dataset[columnName].median()
        descriptive.loc["Mode",columnName]=dataset[columnName].mode()[0]
        descriptive.loc["Q1:25%",columnName]=dataset.describe()[columnName]["25%"]
        descriptive.loc["Q2:50%",columnName]=dataset.describe()[columnName]["50%"]
        descriptive.loc["Q3:75%",columnName]=dataset.describe()[columnName]["75%"]
        descriptive.loc["99%",columnName]=np.percentile(dataset[columnName],99)
        descriptive.loc["Q4:100%",columnName]=dataset.describe()[columnName]["max"]
        descriptive.loc["IQR",columnName]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
        descriptive.loc["1.5Rule",columnName]=1.5*descriptive[columnName]["IQR"]
        descriptive.loc["Lesser",columnName]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5Rule"]
        descriptive.loc["Greater",columnName]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5Rule"]
        descriptive.loc["min",columnName]=dataset[columnName].min()
        descriptive.loc["max",columnName]=dataset[columnName].max()
        descriptive.loc["kurtosis",columnName]=dataset[columnName].kurtosis()
        descriptive.loc["skew",columnName]=dataset[columnName].skew()
        descriptive.loc["var",columnName]=dataset[columnName].var()
        descriptive.loc["std",columnName]=dataset[columnName].std()
    return  descriptive