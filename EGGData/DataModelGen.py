import os
import pandas as pd
import matplotlib.pyplot as plt

confs = os.listdir("D:/Experimento/RawModel_Data")  # get a list of folders

for config in confs:
    # open data for each config
    set1 = pd.read_csv("D:/Experimento/RawModel_Data/" + config + "/set1.csv", header=0)
    set2 = pd.read_csv("D:/Experimento/RawModel_Data/" + config + "/set2.csv", header=0)
    set3 = pd.read_csv("D:/Experimento/RawModel_Data/" + config + "/set3.csv", header=0)

    Gen = pd.DataFrame()

    # Points where the oddball sound appears
    oddballs = [[704, 960, 1280, 1728, 3136],
                [192, 448, 1600, 2112, 3136],
                [1088, 1728, 1856, 2240, 2816]]

    sets = [set1, set2, set3]
    labels = ["set1", "set2", "set3"]

    for i, setx in enumerate(sets):  # Iterate each set
        setx.columns = ["index", "Value"]
        oddball = oddballs[i]
        Setx = pd.DataFrame()
        for x in oddball:
            Setx = pd.concat([Setx, setx["Value"][x:x + 64]])  # Concat each "x" sps after oddball sound

        Setx.reset_index(drop=True, inplace=True)
        print(Setx)
        Setx.columns = [labels[i]]
        Setx.plot(kind="line")

        Gen = pd.concat([Gen, Setx.transpose()])

        # Save a csv of each set and a plot of the signal
        os.makedirs("D:/Experimento/Model_Data64/" + config, exist_ok=True)
        plt.savefig("D:/Experimento/Model_Data64/" + config + "/" + labels[i] + ".png")
        Setx.to_csv("D:/Experimento/Model_Data64/" + config + "/" + labels[i] + ".csv")
        plt.close()

    Gen.to_csv("D:/Experimento/Model_Data64/" + config + "/General.csv")
