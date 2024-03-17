import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_excel(
    r"Lab 2 - Bolted Connections\data_and_analysis.xlsx", sheet_name="plotting"
)

# Plot 'external load vs bolt strain (kN vs unitless)'
plt.figure(1)
plt.plot(
    df[df["dataset"] == "external load vs bolt strain (kN vs unitless)"]["x"],
    df[df["dataset"] == "external load vs bolt strain (kN vs unitless)"]["y"],
    "-ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$\epsilon_b$, Bolt Strain (unitless)")
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\external_load_vs_bolt_strain",
    dpi=300,
    bbox_inches="tight",
)

# Plot 'external load vs washer transducer (kN vs V)'
plt.figure(2)
plt.plot(
    df[df["dataset"] == "external load vs washer transducer (kN vs V)"]["x"],
    df[df["dataset"] == "external load vs washer transducer (kN vs V)"]["y"],
    "-ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$V_w$, Washer Transducer (V)")
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\external_load_vs_washer_transducer",
    dpi=300,
    bbox_inches="tight",
)

# Plot 'torque vs preload (Nm vs kN)'
plt.figure(3)
plt.plot(
    df[df["dataset"] == "torque vs preload (Nm vs kN)"]["x"],
    df[df["dataset"] == "torque vs preload (Nm vs kN)"]["y"],
    "-ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$T$, Torque (Nm)")
plt.ylabel("$F_i$, Preload (kN)")

# Error bars
plt.errorbar(
    df[df["dataset"] == "torque vs preload (Nm vs kN)"]["x"],
    df[df["dataset"] == "torque vs preload (Nm vs kN)"]["y"],
    yerr=df[df["dataset"] == "torque vs preload (Nm vs kN)"]["yerr"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\torque_vs_preload",
    dpi=300,
    bbox_inches="tight",
)

# Plot 'without gasket preseperation (kN vs kN)' and 'without gasket postseperation (kN vs kN)'
plt.figure(4)
plt.plot(
    df[df["dataset"] == "without gasket preseperation (kN vs kN)"]["x"],
    df[df["dataset"] == "without gasket preseperation (kN vs kN)"]["y"],
    "-ko",
    label="Preseperation",
    markersize=6,
    markerfacecolor="none",
)
plt.plot(
    df[df["dataset"] == "without gasket postseperation (kN vs kN)"]["x"],
    df[df["dataset"] == "without gasket postseperation (kN vs kN)"]["y"],
    "--ks",
    label="Postseperation",
    markersize=6,
    markerfacecolor="none",
)

plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$F_i$, Preload (kN)")
plt.legend(loc="upper left")
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\without_gasket_preseperation_vs_postseperation",
    dpi=300,
    bbox_inches="tight",
)

# Plot 'with gasket preseperation (kN vs kN)'
plt.figure(5)
plt.plot(
    df[df["dataset"] == "with gasket preseperation (kN vs kN)"]["x"],
    df[df["dataset"] == "with gasket preseperation (kN vs kN)"]["y"],
    "-ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$F_i$, Preload (kN)")
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\with_gasket_preseperation",
    dpi=300,
    bbox_inches="tight",
)
