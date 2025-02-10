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
    filename = f"../{case}_richardson_cum2.csv"  # Changed filename
    if os.path.exists(filename):
        case_data[case] = pd.read_csv(filename, header=None, delimiter=' ')
    else:
        print(f"Data file for {case} not found.")

# Identify Case 22
case_22 = "AOAp180SDAp340SGPp094SOLn081"

# Plot each case for richardson_cum2
for case, data in case_data.items():
    plt.figure(figsize=(5, 5*0.618))
    
    # Plot all cases in grey first
    flag = 0
    for caseall, dataall in case_data.items():
        plt.plot(dataall.iloc[:,1], dataall.iloc[:,2],  # Column 2 for richardson_cum2
                 ls='-', color='grey', alpha=0.2, 
                 label='Other cases' if flag==0 else None)
        flag = 1
    
    # Plot Case 22 in black
    case_22_data = case_data[case_22]
    plt.plot(case_22_data.iloc[:,1], case_22_data.iloc[:,2],  # Column 3
             lw=2.0, color='k', ls='-', label='Case 22')
    
    # Plot the current case in red
    if not case == "AOAp180SDAp340SGPp094SOLn081":
        plt.plot(data.iloc[:,1], data.iloc[:,2],  # Column 3
                 lw=2.0, ls='-', color='r', label=f'Current Case')
    
    plt.xlim([-0.1, 1.2])
    plt.axvline(1.0, ls='--', label='Trailing edge location')
    plt.xlabel('Flow path length')
    plt.ylabel('$Ri_{c,cum2}$')
    plt.legend(loc='lower left')
    
    # Save the plot
    plt.savefig(f'{case}_richardson_cum2.png')
    plt.close()

print("Plots saved successfully!")
