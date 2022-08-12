import os
import pandas as pd
import matplotlib.pyplot as plt

subjects = os.listdir("D:/Experimento/Raw_data")    # get a list of folders

for sub in subjects:
    # open raw data for each subject
    df = pd.read_csv("D:/Experimento/Raw_data/" + sub + "/Experimento Alerta.csv", header=1)
    # create a new df just for Frontal signals
    frontal = df[['EEG.AF3', 'EEG.F7', 'EEG.F3', 'EEG.FC5', 'EEG.FC6', 'EEG.F4', 'EEG.F8', 'EEG.AF4']]

    # Separate each set in one dataframe
    set1 = frontal[7680:11520]
    set2 = frontal[11520:15360]
    set3 = frontal[15360:]

    Gen = pd.DataFrame()

    # Points where the oddball sound appears
    oddballs = [[768, 1024, 1344, 1792, 3200],
                [256, 512, 1664, 2176, 3200],
                [1152+32, 1792+32, 1920+32, 2304+32, 2880+32]]
    sets = [set1, set2, set3]
    labels = ["set1", "set2", "set3"]
    cols = frontal.columns
    for i, setx in enumerate(sets):     # Iterate each set
        oddball = oddballs[i]
        Setx = pd.DataFrame()
        for col in cols:                # Iterate each Frontal signal in each set
            for x in oddball:
                Setx = pd.concat([Setx, setx[col][x:x + 64]])   # Concat each "x" sps after oddball sound

        Setx.reset_index(drop=True, inplace=True)
        Setx.columns = [labels[i]]
        Setx.plot(kind="line")

        Gen = pd.concat([Gen, Setx.transpose()])

        # Save a csv of each set and a plot of the signal
        os.makedirs("D:/Experimento/Data64/" + sub, exist_ok=True)
        plt.savefig("D:/Experimento/Data64/" + sub + "/" + labels[i] + ".svg", format='svg', dpi=1200)
        Setx.to_csv("D:/Experimento/Data64/" + sub + "/" + labels[i] + ".csv")
        plt.close()

    Gen.to_csv("D:/Experimento/Data128/" + sub + "/General.csv")

