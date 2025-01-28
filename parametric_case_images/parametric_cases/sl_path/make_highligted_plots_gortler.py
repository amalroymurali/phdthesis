import pandas as pd
import matplotlib.pyplot as plt
import os
import plot_style_init

# Read the cases from cases.txt
with open('cases.txt', 'r') as f:
    cases = f.read().splitlines()

# Load data for all cases
case_data = {}
for case in cases:
    filename = f"../{case}_gortler.csv"
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
    	         alpha=0.2, label='Other cases' if flag==0 else None); flag=1
    	if caseall=="AOAp130SDAp360SGPp040SOLn018":
            plt.plot(dataall.iloc[:,1], dataall.iloc[:,2], ls='-', lw=2.0,
                     color='green', label="Case 04")
    # Plot the specific case in color
    plt.plot(data.iloc[:,1], data.iloc[:,2], lw=2.0,
             color='red', label=label)
    #plt.ylim([-1.0e6, 0.5e6])
    plt.xlim([-0.1, 1.2])
    plt.axvline(1.0, ls='--', label='Trailing edge location')
    plt.xlabel('Flow path length')
    plt.ylabel('Gortler Number')
    plt.legend(loc='lower left')
    
    # Save the plot
    plt.savefig(f'{case}_gortler.png')
    plt.close()

print("Plots saved successfully!")
