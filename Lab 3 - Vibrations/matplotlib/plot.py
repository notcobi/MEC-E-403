import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read data from excel
df = pd.read_excel(
    r"Lab 3 - Vibrations\data_and_analysis.xlsx", sheet_name="data for plots"
)
# df['dataset'].unique()
# array(['force vs deflection (N vs m)',
#        'big cart damping ratio trial 1 (zeta vs cycle number)',
#        'big cart damping ratio trial 2 (zeta vs cycle number)',
#        'small cart damping ratio trial 1 (zeta vs cycle number)',
#        'small cart damping ratio trial 2 (zeta vs cycle number)',
#        'small dmf vs omega over p', 'big dmf vs omega over p'],
#       dtype=object)
# plot 1, force vs deflection
plt.figure()
plt.plot(
    df[df["dataset"] == "force vs deflection (N vs m)"]["x"],
    df[df["dataset"] == "force vs deflection (N vs m)"]["y"],
    "o",
    label="Experimental Data",
    markersize=6,
    markerfacecolor="None",
)

# line of best fit through origin
x = df[df["dataset"] == "force vs deflection (N vs m)"]["x"]
y = df[df["dataset"] == "force vs deflection (N vs m)"]["y"]

x = x[:, np.newaxis]
a, _, _, _ = np.linalg.lstsq(x, y, rcond=None)

plt.plot(x, a * x, "k--", label="Line of Best Fit", linewidth=1)
plt.text(0.1, 0.5, f"y = {a[0]:.2f}x")
plt.xlabel("$\delta$, Deflection (m)")
plt.ylabel("$F$, Force (N)")
plt.legend
plt.savefig("Lab 3 - Vibrations/matplotlib/force vs deflection.png")

# plot 2, damping ratio vs cycle number for small cart
plt.figure()
plt.plot(
    df[df["dataset"] == "small cart damping ratio trial 1 (zeta vs cycle number)"]["x"],
    df[df["dataset"] == "small cart damping ratio trial 1 (zeta vs cycle number)"]["y"],
    "ko",
    label="Trial 1",
    markersize=6,
    markerfacecolor="None",
)
plt.plot(
    df[df["dataset"] == "small cart damping ratio trial 2 (zeta vs cycle number)"]["x"],
    df[df["dataset"] == "small cart damping ratio trial 2 (zeta vs cycle number)"]["y"],
    "ks",
    label="Trial 2",
    markersize=6,
    markerfacecolor="None",
)
plt.xlabel("$N$, Cycle Number")
plt.ylabel("$\zeta$, Damping Ratio")
plt.legend()
plt.savefig("Lab 3 - Vibrations/matplotlib/small cart damping ratio.png")

# plot 3, damping ratio vs cycle number for big cart
plt.figure()
plt.plot(
    df[df["dataset"] == "big cart damping ratio trial 1 (zeta vs cycle number)"]["x"],
    df[df["dataset"] == "big cart damping ratio trial 1 (zeta vs cycle number)"]["y"],
    "ko",
    label="Trial 1",
    markersize=6,
    markerfacecolor="None",
)
plt.plot(
    df[df["dataset"] == "big cart damping ratio trial 2 (zeta vs cycle number)"]["x"],
    df[df["dataset"] == "big cart damping ratio trial 2 (zeta vs cycle number)"]["y"],
    "ks",
    label="Trial 2",
    markersize=6,
    markerfacecolor="None",
)
plt.xlabel("$N$, Cycle Number")
plt.ylabel("$\zeta$, Damping Ratio")
plt.legend
plt.savefig("Lab 3 - Vibrations/matplotlib/big cart damping ratio.png")

# plot 4, dmf vs omega over p for small cart
plt.figure()
plt.plot(
    df[df["dataset"] == "small dmf vs omega over p"]["x"],
    df[df["dataset"] == "small dmf vs omega over p"]["y"],
    "ko",
    label="Experimental",
    markersize=6,
    markerfacecolor="None",
)

# plot the theoretical curve
xmin = df[df["dataset"] == "small dmf vs omega over p"]["x"].min()
xmax = df[df["dataset"] == "small dmf vs omega over p"]["x"].max()
x = np.linspace(xmin, xmax, 500)
y = 1 / np.abs(1 - x ** 2)
plt.plot(x, y, "k--", label="Theoretical", linewidth=1)
plt.axvline(x=1, color="r", linestyle="--")
plt.text(0.5, 0.5, 'In Phase')
plt.text(1.2, 0.25, 'Out of Phase')
plt.xlabel("$\omega/p$")
plt.ylabel("$1 / |1 - \omega^2/p^2|$")
plt.ylim(0, 3)
plt.legend
plt.savefig("Lab 3 - Vibrations/matplotlib/small dmf vs omega over p.png")

# plot 5, dmf vs omega over p for big cart
plt.figure()
plt.plot(
    df[df["dataset"] == "big dmf vs omega over p"]["x"],
    df[df["dataset"] == "big dmf vs omega over p"]["y"],
    "ko",
    label="Experimental",
    markersize=6,
    markerfacecolor="None",
)

# plot the theoretical curve
plt.plot(x, y, "k--", label="Theoretical", linewidth=1)
plt.axvline(x=1, color="r", linestyle="--")

plt.text(0.5, 0.5, 'In Phase')
plt.text(1.2, 0.25, 'Out of Phase')
plt.xlabel("$\omega/p$")
plt.ylabel("$1 / |1 - \omega^2/p^2|$")
plt.ylim(0, 3)
plt.legend
plt.savefig("Lab 3 - Vibrations/matplotlib/big dmf vs omega over p.png")



# # find the unique dataset in 'dataset' column
# datasets = df["dataset"].unique()
# x_lables = [
#     '$\delta$, Deflection (m)',
#     '$N$, Cycle Number',
#     '$N$, Cycle Number',
#     '$N$, Cycle Number',
#     '$N$, Cycle Number',
#     '$\omega/p$',
#     '$\omega/p$'
# ]
# y_lables = [
#     '$F$, Force (N)',
#     '$\zeta$, Damping Ratio',
#     '$\zeta$, Damping Ratio',
#     '$\zeta$, Damping Ratio',
#     '$\zeta$, Damping Ratio',
#     '$ 1 / |1 - \omega^2/p^2| $',
#     '$1 / |1 - \omega^2/p^2|$',
# ]

# # make the theoretical dmf curve
# x = np.linspace(0, 2.1, 500)
# y = 1 / np.abs(1 - x ** 2)

# for i, dataset in enumerate(datasets):
#     # filter the dataset
#     df_dataset = df[df["dataset"] == dataset]

#     # plot the dataset
#     plt.figure()
#     plt.plot(df_dataset["x"], df_dataset["y"], "o", label=dataset, markersize=5, markerfacecolor="None")
#     plt.xlabel(x_lables[i])
#     plt.ylabel(y_lables[i])
#     # if dmfs, plot the theoretical curve
#     if "dmf" in dataset:
#         plt.plot(x, y, "k--", label="Theoretical DMF Curve", linewidth=2)
#         # plot vertical line at x=1
#         plt.axvline(x=1, color="r", linestyle="--")
#         plt.legend()

#     plt.savefig(f"Lab 3 - Vibrations/matplotlib/{dataset}.png")
