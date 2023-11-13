# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
#
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')
#
# ##
#
# import matplotlib.pyplot as pl
# import matplotlib.patches as mpatches
# import numpy as np
# import pandas as pd
# from time import time
# from sklearn.metrics import f1_score, accuracy_score
#
# def distribution(data, transformed=False):
#     """
#     Visualization code for displaying skewed distributions of features
#     """
#     # Create figure
#     fig = pl.figure(figsize=(11, 5))
#     # Skewed feature plotting
#     for i, feature in enumerate(['capital-gain', 'capital-loss']):
#         ax = fig.add_subplot(1, 2, i+1)
#         ax.hist(data[feature], bins=25, color='#00A0A0')
#         ax.set_title("'%s' Feature Distribution"%(feature), fontsize=14)
#         ax.set_xlabel("Value")
#         ax.set_ylabel("Number of records")
#         ax.set_ylim((0, 2000))
#         ax.set_yticks([0, 500, 1000, 1500, 2000])
#         ax.set_yticklabels([0, 500, 1000, 1500, ">2000"])
#
#     # Plot aeasthetics
#     if transformed:
#         fig.suptitle("Log-transformed Distributions of Continuous Census Data Features", \
#                      fontsize=16, y=1.03)
#     else:
#         fig.suptitle("Skewed Distributions of Continuous Census Data Features", \
#                      fontsize=16, y=1.03)
#     fig.tight_layout()
#     fig.show()
#
#
# def evaluate(results, accuracy, f1):
#     """
#     Visualization code to display results of various learners.
#     """
#     # Create figure
#     fig, ax = pl.subplots(2, 3, figsize=(11, 8))
#     # Constants
#     bar_width = 0.3
#     colors = ['#A00000','#00A0A0','#00A000']
#     # Super loop to plot four panels of data
#     for k, learner in enumerate(results.keys()):
#         for j, metric in enumerate(['train_time', 'acc_train', 'f_train', 'pred_time', 'acc_test', 'f_test']):
#             for i in np.arange(3):
#                 # Creative plot code
#         ax[j//3, j%3].bar(i + k*bar_width, results[learner][i][metric], width=bar_width, color=colors[k])
#         ax[j//3, j%3].set_xticks([0.45, 1.45, 2.45])
#         ax[j//3, j%3].set_xticklabels(["1%", "10%", "100%"])
#         ax[j//3, j%3].set_xlabel("Training Set Size")
#         ax[j//3, j%3].set_xlim((-0.1, 3.0))
#
#     # add unique y-labels
#     ax[0, 0].set_ylabel("Time (in seconds)")
#     ax[0, 1].set_ylabel("Accuracy score")
#     ax[0, 2].set_ylabel("F-score")
#     ax[1, 0].set_ylabel("Time (in seconds)")
#     ax[1, 1].set_ylabel("Accuracy score")
#     ax[1, 2].set_ylabel("F-score")
#
#     # add titles
#     ax[0, 0].set_title("Model training")
#     ax[0, 1].set_title("Accuracy score on training subset")
#     ax[0, 2].set_title("F-score on training subset")
#     ax[1, 0].set_title("Model predicting")
#     ax[1, 1].set_title("Accuracy score on testing set")
#     ax[1, 2].set_title("F-score on testing set")
#
#