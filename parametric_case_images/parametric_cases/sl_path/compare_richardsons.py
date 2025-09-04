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
    filename = f"../{case}_richardson.csv"
    if os.path.exists(filename):
        case_data[case] = pd.read_csv(filename, header=None, delimiter=' ')
    else:
        print(f"Data file for {case} not found.")

# Plot each case separately
plt.figure(figsize=(5, 5*0.618))
flag=0
for caseall, dataall in case_data.items():
    plt.plot(dataall.iloc[:,1], dataall.iloc[:,2], ls='-',color='grey',
    	     alpha=0.2, label='Other cases' if flag==0 else None);flag=1
for case, data in case_data.items():

    if case=="AOAp140SDAp352SGPp071SOLp030":
        label = "Case 05"
        plt.plot(data.iloc[:,1], data.iloc[:,2], ls='-', lw=1.0,
                 label=label)
    elif case=="AOAp190SDAp320SGPp064SOLn009":
        label = "Case 29"
        plt.plot(data.iloc[:,1], data.iloc[:,2], ls='-', lw=1.0,
                 label=label)
    elif case=="AOAp180SDAp340SGPp094SOLn081":
        label = "Case 22"
        plt.plot(data.iloc[:,1], data.iloc[:,2], ls='-', lw=1.0,
                 label=label)
    elif case=="AOAp164SDAp352SGPp043SOLn023":
        label = "Case 11"
        plt.plot(data.iloc[:,1], data.iloc[:,2], ls='-', lw=1.0,
                 label=label)
    else:
        label = "Case"

plt.ylim([-1.0, 2])
plt.xlim([-0.1, 1.2])
plt.axvline(1.0, ls='--', label='Trailing edge location')
plt.xlabel('Flow path length')
plt.ylabel('$Ri_{c}=\\frac{2U}{R}/[\\frac{\\partial U}{\\partial n}+\\frac{U}{R}]$')
plt.legend(loc='lower left')
    
# Save the plot
plt.savefig(f'Compare_richardsons.png')
plt.close()

print("Plots saved successfully!")
