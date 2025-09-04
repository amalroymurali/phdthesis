for casename in $(cat ./cases.txt); do
      
    rsync newton-cascade:/home/lmfa/amurali/Bureau/MAMBO/ValiantCFD/LBM/Database/hot_wire_probe_SL/${casename}/Zvel/spanwise_plot_probe_17.png ./${casename}_probe_17.png
    
    done
