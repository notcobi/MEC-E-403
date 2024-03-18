import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_excel(
    r"Lab 2 - Bolted Connections\data_and_analysis.xlsx", sheet_name="plotting"
)

# Plot 'external load vs bolt strain (kN vs unitless)'
plt.figure(1)

# Linear fit
x = df[df["dataset"] == "external load vs bolt strain (kN vs unitless)"]["x"]
y = df[df["dataset"] == "external load vs bolt strain (kN vs unitless)"]["y"]
a, _, _, _ = np.linalg.lstsq(x[:, np.newaxis], y, rcond=None)

# Plot linear fit
plt.plot(x, a * x, "--k", label="Linear Fit")
plt.plot(
    df[df["dataset"] == "external load vs bolt strain (kN vs unitless)"]["x"],
    df[df["dataset"] == "external load vs bolt strain (kN vs unitless)"]["y"],
    "ko",
    markersize=6,
    markerfacecolor="none",
)
plt.text(x.iloc[len(x) // 2] + 0.5, a * x.iloc[len(x) // 2], f"$\epsilon_b = ({a[0]:.2E})P$", fontsize=12)
plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$\epsilon_b$, Bolt Strain (unitless)")
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\external_load_vs_bolt_strain",
    dpi=300,
    bbox_inches="tight",
)

# Plot 'external load vs washer transducer (kN vs V)'
plt.figure(2)

# Linear fit
x = df[df["dataset"] == "external load vs washer transducer (kN vs V)"]["x"]
y = df[df["dataset"] == "external load vs washer transducer (kN vs V)"]["y"]
a, _, _, _ = np.linalg.lstsq(x[:, np.newaxis], y, rcond=None)

plt.plot(x, a * x, "--k", label="Linear Fit")
plt.plot(
    df[df["dataset"] == "external load vs washer transducer (kN vs V)"]["x"],
    df[df["dataset"] == "external load vs washer transducer (kN vs V)"]["y"],
    "ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$V_w$, Washer Transducer (V)")
plt.text(x.iloc[len(x) // 2] + 0.5, a * x.iloc[len(x) // 2], f"$V_w = ({a[0]:.2E})P$", fontsize=12)
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\external_load_vs_washer_transducer",
    dpi=300,
    bbox_inches="tight",
)

# Plot 'torque vs preload (Nm vs kN)'
plt.figure(3)

# Linear fit
x = df[df["dataset"] == "torque vs preload (Nm vs kN)"]["x"]
y = df[df["dataset"] == "torque vs preload (Nm vs kN)"]["y"]
a, _, _, _ = np.linalg.lstsq(x[:, np.newaxis], y, rcond=None)

plt.plot(x, a * x, "--k", label="Linear Fit")
plt.plot(
    df[df["dataset"] == "torque vs preload (Nm vs kN)"]["x"],
    df[df["dataset"] == "torque vs preload (Nm vs kN)"]["y"],
    "ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$T$, Torque (Nm)")
plt.ylabel("$F_i$, Preload (kN)")
plt.text(x.iloc[len(x) // 2] + 0.5, a * x.iloc[len(x) // 2], f"$F_i = ({a[0]:.2E})T$", fontsize=12)

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

# Linear fits
x1 = df[df["dataset"] == "without gasket preseperation (kN vs kN)"]["x"]
y1 = df[df["dataset"] == "without gasket preseperation (kN vs kN)"]["y"]
a1, b1 = np.polyfit(x1, y1, 1)

x2 = df[df["dataset"] == "without gasket postseperation (kN vs kN)"]["x"]
y2 = df[df["dataset"] == "without gasket postseperation (kN vs kN)"]["y"]
a2, b2 = np.polyfit(x2, y2, 1)

plt.plot(x1, a1 * x1 + b1, "--k", label="Preseperation Linear Fit")
plt.plot(x2, a2 * x2 + b2, "-.k", label="Postseperation Linear Fit")
plt.plot(
    df[df["dataset"] == "without gasket preseperation (kN vs kN)"]["x"],
    df[df["dataset"] == "without gasket preseperation (kN vs kN)"]["y"],
    "ko",
    label="Preseperation",
    markersize=6,
    markerfacecolor="none",
)
plt.plot(
    df[df["dataset"] == "without gasket postseperation (kN vs kN)"]["x"],
    df[df["dataset"] == "without gasket postseperation (kN vs kN)"]["y"],
    "ks",
    label="Postseperation",
    markersize=6,
    markerfacecolor="none",
)
plt.text(x1.iloc[len(x1) // 2] + 1.2, a1 * x1.iloc[len(x1) // 2] + b1, f"$F_i = ({a1:.2E})P + {b1:.2f}$", fontsize=12)
plt.text(x2.iloc[len(x2) // 2] - 5.5, a2 * x2.iloc[len(x2) // 2] + b2 - 1, f"$F_i = ({a2:.2E})P + {b2:.2E}$", fontsize=12)

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

# Linear fit
x = df[df["dataset"] == "with gasket preseperation (kN vs kN)"]["x"]
y = df[df["dataset"] == "with gasket preseperation (kN vs kN)"]["y"]
a1, b1 = np.polyfit(x, y, 1)

# Quadratic fit
a2, b2, c2 = np.polyfit(x, y, 2)

plt.plot(x, a1 * x + b1, "--k", label="Linear Fit")
plt.plot(x, a2 * x ** 2 + b2 * x + c2, ":k", label="Quadratic Fit")
plt.plot(
    df[df["dataset"] == "with gasket preseperation (kN vs kN)"]["x"],
    df[df["dataset"] == "with gasket preseperation (kN vs kN)"]["y"],
    "ko",
    markersize=6,
    markerfacecolor="none",
)
plt.xlabel("$P$, External Load (kN)")
plt.ylabel("$F_i$, Preload (kN)")
plt.text(0.9, 5.5, f"$F_i = ({a1:.2E})P + {b1:.2f}$", fontsize=12)
plt.text(2, 4 , f"$F_i = ({a2:.2E})P^2 + ({b2:.2E})P + {c2:.2f}$", fontsize=12)
plt.legend(loc="upper left")
plt.savefig(
    r"Lab 2 - Bolted Connections\Sections\Figures\with_gasket_preseperation",
    dpi=300,
    bbox_inches="tight",
)
