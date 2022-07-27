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

    # Points where the oddball sound appears
    oddballs = [[768, 1024, 1344, 1792, 3200],
                [768, 1024, 1344, 1792, 3200],
                [768+25, 1024+25, 1344+25, 1792+25, 3200+25]]
    sets = [set1, set2, set3]
    labels = ["set1", "set2", "set3"]
    cols = frontal.columns
    for i, setx in enumerate(sets):     # Iterate each set
        oddball = oddballs[i]
        Setx = pd.DataFrame()
        for col in cols:                # Iterate each Frontal signal in each set
            for x in oddball:
                Setx = pd.concat([Setx, setx[col][x:x + 64]])   # Concate each 64 sps after oddball sound

        Setx.reset_index(drop=True, inplace=True)
        Setx.columns = [labels[i]]
        Setx.plot(kind="line")
        plt.close()

        # Save a csv of each set and a plot of the signal
        os.makedirs("D:/Experimento/Data/" + sub, exist_ok=True)
        plt.savefig("D:/Experimento/Data/" + sub + "/" + labels[i] + ".png")
        Setx.to_csv("D:/Experimento/Data/" + sub + "/" + labels[i] + ".csv")
