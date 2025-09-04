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
    filename = f"../{case}_criticalrat.csv"
    if os.path.exists(filename):
        case_data[case] = pd.read_csv(filename, header=None, delimiter=' ')
    else:
        print(f"Data file for {case} not found.")

# Plot each case separately
for case, data in case_data.items():
    plt.figure()

    # Plot all cases in grey
    flag=0
    for caseall, dataall in case_data.items():
    	plt.plot(dataall.iloc[:,1], dataall.iloc[:,2], ls='-',color='grey',
    	         alpha=0.2, label='All cases' if flag==0 else None); flag=1

    # Plot the specific case in color
    plt.plot(data.iloc[:,1], data.iloc[:,2], lw=2.0,
             color='blue', label="Case")

    
    plt.axhspan(ymin=-1, ymax=0.425, ls='-', color='red', alpha=0.3)
    plt.axhspan(ymin=0.425, ymax=0.455, ls='-', color='orange', alpha=0.3)
    plt.axhspan(ymin=0.455, ymax=0.8, ls='-', color='green', alpha=0.3)
    plt.ylim([-0.1, 0.7])
    plt.xlabel('Flow path length')
    plt.ylabel('Critical Ratio $M_l^*$')
    plt.legend(loc='upper left')
    
    # Save the plot
    plt.savefig(f'{case}_criticalrat.png')
    plt.close()

print("Plots saved successfully!")
