import pandas as pd
import matplotlib.pyplot as plt
import os
import plot_style_init

# Read the cases from cases.txt
with open('cases.txt', 'r') as f:
    cases = f.read().splitlines()
non_noisy_cases = [
    "AOAp130SDAp360SGPp040SOLn018",
    "AOAp140SDAp352SGPp071SOLp030",
    "AOAp147SDAp352SGPp093SOLp076",
    "AOAp152SDAp352SGPp063SOLp072",
    "AOAp159SDAp352SGPp067SOLp051",
    "AOAp164SDAp352SGPp043SOLp023",
    "AOAp174SDAp352SGPp085SOLp049",
    "AOAp186SDAp352SGPp048SOLp032",
    "AOAp192SDAp352SGPp053SOLp063",
    "AOAp181SDAp352SGPp078SOLp059"
]

# Load data for all cases
case_data = {}
for case in cases:
    filename = f"../{case}_curvr.csv"
    if os.path.exists(filename):
        case_data[case] = pd.read_csv(filename, header=None, delimiter=' ')
    else:
        print(f"Data file for {case} not found.")

# Plot each case separately
for case, data in case_data.items():
    plt.figure(figsize=(5, 5*0.618))

    if case=="AOAp180SDAp340SGPp094SOLn081":
        label = "Case 22"
    elif case=="AOAp152SDAp352SGPp063SOLp072":
        label = "Case 08"
    else:
        label = "Case"
    # Plot all cases in grey
    flag=0
    for caseall, dataall in case_data.items():
    	plt.plot(dataall.iloc[:,1], dataall.iloc[:,2], ls='-',color='grey',
    	         alpha=0.2, label='All cases' if flag==0 else None); flag=1

    # Plot the specific case in color
    plt.plot(data.iloc[:,1], data.iloc[:,2], lw=2.0,
             color='red', label=label)
    plt.ylim([-50, 500])
    plt.xlim([-0.1, 1.2])
    plt.axvline(1.0, ls='--', label='Trailing edge location')
    plt.xlabel('Flow path length')
    plt.ylabel('Curvature ($\\frac{1}{\sqrt{(d^2x/ds^2)^2 + (d^2y/ds^2)^2}}$)($m^{-1}$)')
    plt.legend(loc='upper left')
    if case in non_noisy_cases:
        plt.gca().set_facecolor((0.0, 0.6, 0.0, 0.1))
    else:
        plt.gca().set_facecolor((0.6, 0.0, 0.0, 0.1))

    # Save the plot
    plt.savefig(f'{case}_curvr.png')
    plt.close()

print("Plots saved successfully!")
