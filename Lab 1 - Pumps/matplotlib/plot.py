import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_csv(r'Lab 6\matplotlib\calibration.csv')

# Sort Thermistor data
df_thermistor = df[['Thermistor Temperature', 'Thermistor Voltage']]

# Sort Thermocouple data
df_thermocouple = df[['Thermocouple Temperature', 'Thermocouple Voltage']]

# Linear regression for Thermistor
thermistor_fit = np.polyfit(df_thermistor['Thermistor Voltage'], df_thermistor['Thermistor Temperature'], 1)
thermistor_fit_fn = np.poly1d(thermistor_fit)

# Linear regression for Thermocouple
thermocouple_fit = np.polyfit(df_thermocouple['Thermocouple Voltage'], df_thermocouple['Thermocouple Temperature'], 1)
thermocouple_fit_fn = np.poly1d(thermocouple_fit)

# Plot the Thermistor data and linear regression
plt.figure(1)
plt.plot(df_thermistor['Thermistor Voltage'], df_thermistor['Thermistor Temperature'], 'ko', label='Thermistor Data', markersize=6, markerfacecolor='none')
plt.plot(df_thermistor['Thermistor Voltage'], thermistor_fit_fn(df_thermistor['Thermistor Voltage']), 'k--', label='Thermistor Linear Regression')
plt.xlabel(r'$V$, Voltage (V)')
plt.ylabel(r'$T$, Temperature ($^\circ$C)')
plt.legend(loc='upper left')
plt.text(1.42, 30, r'$T = ' + str(round(thermistor_fit[0], 2)) + 'V  ' + str(round(thermistor_fit[1], 2)) + '$')
plt.savefig(r'Lab 6\matplotlib\thermistor.png', dpi=300)

# Plot the Thermocouple data and linear regression
plt.figure(2)
plt.plot(df_thermocouple['Thermocouple Voltage'], df_thermocouple['Thermocouple Temperature'], 'ko', label='Thermocouple Data', markersize=6, markerfacecolor='none')
plt.plot(df_thermocouple['Thermocouple Voltage'], thermocouple_fit_fn(df_thermocouple['Thermocouple Voltage']), 'k--', label='Thermocouple Linear Regression')
plt.xlabel(r'$V$, Voltage (V)')
plt.ylabel(r'$T$, Temperature ($^\circ$C)')
plt.legend(loc='upper left')
plt.text(1.425, 30, r'$T = ' + str(round(thermocouple_fit[0], 2)) + 'V  ' + str(round(thermocouple_fit[1], 2)) + '$')
plt.savefig(r'Lab 6\matplotlib\thermocouple.png', dpi=300)

# ----------------------------------------
# 	Air		Water	
# 	Thermistor	Thermocouple	Thermistor	Thermocouple
# T_0	48.457	48.418	39.914	42.617
# T_infty	21.759	23.281	20.691	20.059
# tau	18.69803057	18.02662691	0.373547583	0.225033996
# SS	122.338	46.26568305	35.74509399	69.88833339
# The first order response of the system is 
# \begin{equation*}
#     T = T_{\infty} + (T_0 - T_{\infty})e^{-t/\tau}
# \end{equation*}

# Read data from csv file
df = pd.read_csv(r'Lab 6\matplotlib\transient_air.csv')

# Sort Thermistor data
df_thermistor = df[['Time', 'Thermistor Temperature', 'Thermistor Response']]

# Sort Thermocouple data
df_thermocouple = df[['Time', 'Thermocouple Temperature', 'Thermocouple Response']]

# Plot the Thermistor data and Response
plt.figure(3)
plt.plot(df_thermistor['Time'], df_thermistor['Thermistor Temperature'], 'ko', label='Thermistor Temperature', markersize=6, markerfacecolor='none')
plt.plot(df_thermistor['Time'], df_thermistor['Thermistor Response'], 'k--', label='Thermistor Fit')
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$T$, Temperature ($^\circ$C)')
plt.legend(loc='upper right')
plt.text(40, 30, r'$T = 21.759 + 26.698e^{-t/18.698}$')
plt.savefig(r'Lab 6\matplotlib\thermistor_transient_air.png', dpi=300)

# Plot the Thermocouple data and Response
plt.figure(4)
plt.plot(df_thermocouple['Time'], df_thermocouple['Thermocouple Temperature'], 'ko', label='Thermocouple Temperature', markersize=6, markerfacecolor='none')
plt.plot(df_thermocouple['Time'], df_thermocouple['Thermocouple Response'], 'k--', label='Thermocouple Fit')
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$T$, Temperature ($^\circ$C)')
plt.legend(loc='upper right')
plt.text(40, 30, r'$T = 23.281 + 25.137e^{-t/18.027}$')
plt.savefig(r'Lab 6\matplotlib\thermocouple_transient_air.png', dpi=300)

# Read data from csv file
df = pd.read_csv(r'Lab 6\matplotlib\transient_water.csv')

# Sort Thermistor data
df_thermistor = df[['Time', 'Thermistor Temperature', 'Thermistor Response']]

# Sort Thermocouple data
df_thermocouple = df[['Time', 'Thermocouple Temperature', 'Thermocouple Response']]

# Plot the Thermistor data and Response
plt.figure(5)
plt.plot(df_thermistor['Time'], df_thermistor['Thermistor Temperature'], 'ko', label='Thermistor Temperature', markersize=6, markerfacecolor='none')
plt.plot(df_thermistor['Time'], df_thermistor['Thermistor Response'], 'k--', label='Thermistor Fit')
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$T$, Temperature ($^\circ$C)')
plt.legend(loc='upper right')
plt.text(0.5, 30, r'$T = 20.691 + 19.223e^{-t/0.374}$')
plt.savefig(r'Lab 6\matplotlib\thermistor_transient_water.png', dpi=300)

# Plot the Thermocouple data and Response
plt.figure(6)
plt.plot(df_thermocouple['Time'], df_thermocouple['Thermocouple Temperature'], 'ko', label='Thermocouple Temperature', markersize=6, markerfacecolor='none')
plt.plot(df_thermocouple['Time'], df_thermocouple['Thermocouple Response'], 'k--', label='Thermocouple Fit')
plt.xlabel(r'$t$, Time (s)')
plt.ylabel(r'$T$, Temperature ($^\circ$C)')
plt.legend(loc='upper right')
plt.text(0.5, 30, r'$T = 20.059 + 22.558e^{-t/0.225}$')
plt.savefig(r'Lab 6\matplotlib\thermocouple_transient_water.png', dpi=300)
plt.show()
