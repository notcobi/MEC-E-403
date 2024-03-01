import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_csv(r"Lab 1 - Pumps\matplotlib\single, parallel, series.csv")

# Sort Pump Data
df_single = df[
    (df["Pump Configuration"] == "Single") & (df["Data Type"] == "Experimental")
]
df_parallel = df[
    (df["Pump Configuration"] == "Parallel") & (df["Data Type"] == "Experimental")
]
df_series = df[
    (df["Pump Configuration"] == "Series") & (df["Data Type"] == "Experimental")
]
df_parallel_theoretical = df[
    (df["Pump Configuration"] == "Parallel") & (df["Data Type"] == "Theoretical")
]
df_series_theoretical = df[
    (df["Pump Configuration"] == "Series") & (df["Data Type"] == "Theoretical")
]
df_manufacturer = df[
    (df["Data Type"] == "Manufacturer") & (df["Pump Configuration"] == "Single")
]
df_geometrically_similar = df[(df["Data Type"] == "Geometrically Similar")]
df_geometrically_dissimilar = df[(df["Data Type"] == "Geometrically Dissimilar")]
# ----------------------------------------
# Plot the Single Pump Head and Flow Rate
plt.figure(1)
plt.plot(
    df_single[df_single["Pump Speed"] == 1800]["Volumetric Flow"],
    df_single[df_single["Pump Speed"] == 1800]["Corrected Head"],
    "-ko",
    label="1800 RPM",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_single[df_single["Pump Speed"] == 2700]["Volumetric Flow"],
    df_single[df_single["Pump Speed"] == 2700]["Corrected Head"],
    "-k^",
    label="2700 RPM",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_single[df_single["Pump Speed"] == 3600]["Volumetric Flow"],
    df_single[df_single["Pump Speed"] == 3600]["Corrected Head"],
    "-ks",
    label="3600 RPM",
    markersize=6,
    markerfacecolor="k",
)

# Error bars
plt.errorbar(
    df_single[df_single["Pump Speed"] == 1800]["Volumetric Flow"],
    df_single[df_single["Pump Speed"] == 1800]["Corrected Head"],
    xerr=df_single[df_single["Pump Speed"] == 1800]["Flow Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 1800]["Head Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)
plt.errorbar(
    df_single[df_single["Pump Speed"] == 2700]["Volumetric Flow"],
    df_single[df_single["Pump Speed"] == 2700]["Corrected Head"],
    xerr=df_single[df_single["Pump Speed"] == 2700]["Flow Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 2700]["Head Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)
plt.errorbar(
    df_single[df_single["Pump Speed"] == 3600]["Volumetric Flow"],
    df_single[df_single["Pump Speed"] == 3600]["Corrected Head"],
    xerr=df_single[df_single["Pump Speed"] == 3600]["Flow Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 3600]["Head Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

plt.xlabel(r"$Q$, Volumetric Flow Rate ($m^3 s^{-1}$)")
plt.ylabel(r"$H$, Corrected Head (m)")
plt.legend(loc="upper right")
plt.savefig(r"Lab 1 - Pumps\Sections\Figures\Single Pump Plot", dpi=300)

# ----------------------------------------
# Plot the Single Pump Head coefficient and flow coefficient
plt.figure(2)
plt.plot(
    df_single[df_single["Pump Speed"] == 1800]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 1800]["Head Coeff"],
    "-ko",
    label="Exp. 1800 RPM",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_single[df_single["Pump Speed"] == 2700]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 2700]["Head Coeff"],
    "-k^",
    label="Exp. 2700 RPM",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_single[df_single["Pump Speed"] == 3600]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 3600]["Head Coeff"],
    "-ks",
    label="Exp. 3600 RPM",
    markersize=6,
    markerfacecolor="k",
)

# Error bars
plt.errorbar(
    df_single[df_single["Pump Speed"] == 1800]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 1800]["Head Coeff"],
    xerr=df_single[df_single["Pump Speed"] == 1800]["Flow Coeff Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 1800]["Head Coeff Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

plt.errorbar(
    df_single[df_single["Pump Speed"] == 2700]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 2700]["Head Coeff"],
    xerr=df_single[df_single["Pump Speed"] == 2700]["Flow Coeff Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 2700]["Head Coeff Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

plt.errorbar(
    df_single[df_single["Pump Speed"] == 3600]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 3600]["Head Coeff"],
    xerr=df_single[df_single["Pump Speed"] == 3600]["Flow Coeff Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 3600]["Head Coeff Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

# Plot the manufacturer data
plt.plot(
    df_manufacturer[df_manufacturer["Pump Speed"] == 1800]["Flow Coeff"],
    df_manufacturer[df_manufacturer["Pump Speed"] == 1800]["Head Coeff"],
    "--ko",
    label="Manu. 1800 RPM",
    markersize=6,
    markerfacecolor="none",
)
plt.plot(
    df_manufacturer[df_manufacturer["Pump Speed"] == 2700]["Flow Coeff"],
    df_manufacturer[df_manufacturer["Pump Speed"] == 2700]["Head Coeff"],
    "--k^",
    label="Manu. 2700 RPM",
    markersize=6,
    markerfacecolor="none",
)
plt.plot(
    df_manufacturer[df_manufacturer["Pump Speed"] == 3600]["Flow Coeff"],
    df_manufacturer[df_manufacturer["Pump Speed"] == 3600]["Head Coeff"],
    "--ks",
    label="Manu. 3600 RPM",
    markersize=6,
    markerfacecolor="none",
)

# Plot Ideal Line
# Psi = 1 - 1.53986496 * Phi
PhiMax = 0.147119554
PhiMin = 0
Phi = np.linspace(PhiMin, PhiMax, 25)
Psi = 1 - 1.53986496 * Phi

plt.plot(Phi, Psi, "-k", label="Ideal Line")

plt.xlabel(r"$\Phi$, Flow Coefficient (unitless)")
plt.ylabel(r"$\Psi$, Head Coefficient (unitless)")
plt.legend(loc="upper right")
plt.savefig(r"Lab 1 - Pumps\Sections\Figures\Single Pump Coefficients Plot", dpi=300)

# ----------------------------------------
# Plot the Parallel Pump Head and Flow Rate
plt.figure(3)
plt.plot(
    df_parallel[df_parallel["Pump Speed"] == 2700]["Volumetric Flow"],
    df_parallel[df_parallel["Pump Speed"] == 2700]["Corrected Head"],
    "-ko",
    label="Experimental",
    markersize=6,
    markerfacecolor="k",
)

# Error bars
plt.errorbar(
    df_parallel[df_parallel["Pump Speed"] == 2700]["Volumetric Flow"],
    df_parallel[df_parallel["Pump Speed"] == 2700]["Corrected Head"],
    xerr=df_parallel[df_parallel["Pump Speed"] == 2700]["Flow Uncertainty"],
    # yerr = df_parallel[df_parallel["Pump Speed"] == 2700]["Head Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

# Theoretical Data
plt.plot(
    df_parallel_theoretical[df_parallel_theoretical["Pump Speed"] == 2700][
        "Volumetric Flow"
    ],
    df_parallel_theoretical[df_parallel_theoretical["Pump Speed"] == 2700][
        "Corrected Head"
    ],
    "--k^",
    label="Theoretical",
    markersize=6,
    markerfacecolor="none",
)

plt.xlabel(r"$Q$, Volumetric Flow Rate ($m^3 s^{-1}$)")
plt.ylabel(r"$H$, Corrected Head (m)")
plt.legend(loc="upper right")
plt.savefig(r"Lab 1 - Pumps\Sections\Figures\Parallel Pump Plot", dpi=300)

# ----------------------------------------
# Plot the Series Pump Head and Flow Rate
plt.figure(4)
plt.plot(
    df_series[df_series["Pump Speed"] == 2700]["Volumetric Flow"],
    df_series[df_series["Pump Speed"] == 2700]["Corrected Head"],
    "-ko",
    label="Experimental",
    markersize=6,
    markerfacecolor="k",
)

# Error bars
plt.errorbar(
    df_series[df_series["Pump Speed"] == 2700]["Volumetric Flow"],
    df_series[df_series["Pump Speed"] == 2700]["Corrected Head"],
    xerr=df_series[df_series["Pump Speed"] == 2700]["Flow Uncertainty"],
    # yerr = df_series[df_series["Pump Speed"] == 2700]["Head Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

# Theoretical Data
plt.plot(
    df_series_theoretical[df_series_theoretical["Pump Speed"] == 2700][
        "Volumetric Flow"
    ],
    df_series_theoretical[df_series_theoretical["Pump Speed"] == 2700][
        "Corrected Head"
    ],
    "--k^",
    label="Theoretical",
    markersize=6,
    markerfacecolor="none",
)

plt.xlabel(r"$Q$, Volumetric Flow Rate ($m^3 s^{-1}$)")
plt.ylabel(r"$H$, Corrected Head (m)")
plt.legend(loc="upper right")
plt.savefig(r"Lab 1 - Pumps\Sections\Figures\Series Pump Plot", dpi=300)

# ----------------------------------------
# Plot the Geometrically Similar Pump Head Coefficient and Flow Coefficient
plt.figure(5)
plt.plot(
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.108][
        "Flow Coeff"
    ],
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.108][
        "Head Coeff"
    ],
    "-ko",
    label="108 mm",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.102][
        "Flow Coeff"
    ],
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.102][
        "Head Coeff"
    ],
    "--k^",
    label="102 mm",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.096][
        "Flow Coeff"
    ],
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.096][
        "Head Coeff"
    ],
    "-.ks",
    label="96 mm",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.083][
        "Flow Coeff"
    ],
    df_geometrically_similar[df_geometrically_similar["Impeller Diameter"] == 0.083][
        "Head Coeff"
    ],
    "-kx",
    label="83 mm",
    markersize=6,
    markerfacecolor="k",
)

plt.xlabel(r"$\Phi$, Flow Coefficient (unitless)")
plt.ylabel(r"$\Psi$, Head Coefficient (unitless)")
plt.legend(loc="upper right")
plt.savefig(
    r"Lab 1 - Pumps\Sections\Figures\Geometrically Similar Pump Coefficients Plot",
    dpi=300,
)

# ----------------------------------------
# Plot the Geometrically Dissimilar Pump Head Coefficient and Flow Coefficient
plt.figure(6)
plt.plot(
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.108
    ]["Flow Coeff"],
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.108
    ]["Head Coeff"],
    "-ko",
    label="108 mm",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.102
    ]["Flow Coeff"],
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.102
    ]["Head Coeff"],
    "--k^",
    label="102 mm",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.096
    ]["Flow Coeff"],
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.096
    ]["Head Coeff"],
    "-.ks",
    label="96 mm",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.083
    ]["Flow Coeff"],
    df_geometrically_dissimilar[
        df_geometrically_dissimilar["Impeller Diameter"] == 0.083
    ]["Head Coeff"],
    "-kx",
    label="83 mm",
    markersize=6,
    markerfacecolor="k",
)

plt.xlabel(r"$\Phi$, Flow Coefficient (unitless)")
plt.ylabel(r"$\Psi$, Head Coefficient (unitless)")
plt.legend(loc="upper right")
plt.savefig(
    r"Lab 1 - Pumps\Sections\Figures\Geometrically Dissimilar Pump Coefficients Plot",
    dpi=300,
)

# ----------------------------------------
# Single Pump Efficiency
plt.figure(7)
plt.plot(
    df_single[df_single["Pump Speed"] == 1800]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 1800]["Efficiency"],
    "-ko",
    label="Exp. 1800 RPM",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_single[df_single["Pump Speed"] == 2700]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 2700]["Efficiency"],
    "-k^",
    label="Exp. 2700 RPM",
    markersize=6,
    markerfacecolor="k",
)
plt.plot(
    df_single[df_single["Pump Speed"] == 3600]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 3600]["Efficiency"],
    "-ks",
    label="Exp. 3600 RPM",
    markersize=6,
    markerfacecolor="k",
)

# Error bars
plt.errorbar(
    df_single[df_single["Pump Speed"] == 1800]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 1800]["Efficiency"],
    xerr=df_single[df_single["Pump Speed"] == 1800]["Flow Coeff Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 1800]["Efficiency Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)
plt.errorbar(
    df_single[df_single["Pump Speed"] == 2700]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 2700]["Efficiency"],
    xerr=df_single[df_single["Pump Speed"] == 2700]["Flow Coeff Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 2700]["Efficiency Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)
plt.errorbar(
    df_single[df_single["Pump Speed"] == 3600]["Flow Coeff"],
    df_single[df_single["Pump Speed"] == 3600]["Efficiency"],
    xerr=df_single[df_single["Pump Speed"] == 3600]["Flow Coeff Uncertainty"],
    # yerr = df_single[df_single["Pump Speed"] == 3600]["Efficiency Uncertainty"],
    fmt="none",
    ecolor="k",
    capsize=5,
    elinewidth=1,
    capthick=1,
)

# Manufacturer Data
plt.plot(
    df_manufacturer[df_manufacturer["Pump Speed"] == 1800]["Flow Coeff"],
    df_manufacturer[df_manufacturer["Pump Speed"] == 1800]["Efficiency"],
    "--ko",
    label="Manu. 1800 RPM",
    markersize=6,
    markerfacecolor="none",
)
plt.plot(
    df_manufacturer[df_manufacturer["Pump Speed"] == 2700]["Flow Coeff"],
    df_manufacturer[df_manufacturer["Pump Speed"] == 2700]["Efficiency"],
    "--k^",
    label="Manu. 2700 RPM",
    markersize=6,
    markerfacecolor="none",
)
plt.plot(
    df_manufacturer[df_manufacturer["Pump Speed"] == 3600]["Flow Coeff"],
    df_manufacturer[df_manufacturer["Pump Speed"] == 3600]["Efficiency"],
    "--ks",
    label="Manu. 3600 RPM",
    markersize=6,
    markerfacecolor="none",
)

plt.xlabel(r"$\Phi$, Flow Coefficient (unitless)")
plt.ylabel(r"$\eta$, Efficiency (%)")
plt.legend(loc="lower right")
plt.savefig(r"Lab 1 - Pumps\Sections\Figures\Single Pump Efficiency Plot", dpi=300)
