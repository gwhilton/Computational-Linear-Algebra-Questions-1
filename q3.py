import numpy as np 
from cla_utils import *
import matplotlib.pyplot as plt
from tabulate import tabulate
from q3func import *

#########################################Generating Graphs for Analysis###########################################

#3a
householder_plot_5(10)
householder_plot_5(50)
householder_plot_5(200) 

#3b
#p=5
HH_QR_plot(200,5)
GSM_QR_plot(200,5)
GSC_QR_plot(200,5)

#p=10
HH_QR_plot(200,15)
GSM_QR_plot(200,15)
GSC_QR_plot(200,15)

#p=25
HH_QR_plot(200,25)
GSM_QR_plot(200,25)
GSC_QR_plot(200,25)

#p=50
HH_QR_plot(200,50)
GSM_QR_plot(200,50)
GSC_QR_plot(200,50)

#p=100
HH_QR_plot(200,150)
GSM_QR_plot(200,150)
GSC_QR_plot(200,150)

