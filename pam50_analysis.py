import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = 'denseDataOnlyDownload-2.tsv'  # Use the correct path to your TSV file
df = pd.read_csv(file_path, sep='\t')

# Select a gene for differential expression analysis
gene_of_interest = 'ERBB2'  # Replace with the gene of interest

# Perform t-tests between all subtypes for the selected gene
subtypes = df['PAM50Call_RNAseq'].unique()
subtype_pairs = [(subtypes[i], subtypes[j]) for i in range(len(subtypes)) for j in range(i+1, len(subtypes))]
p_values = []

for subtype_pair in subtype_pairs:
    data1 = df[df['PAM50Call_RNAseq'] == subtype_pair[0]][gene_of_interest]
    data2 = df[df['PAM50Call_RNAseq'] == subtype_pair[1]][gene_of_interest]
    stat, p_val = ttest_ind(data1, data2)
    p_values.append((subtype_pair[0], subtype_pair[1], p_val))

# Adjust for multiple testing using Benjamini-Hochberg
p_vals = [p[2] for p in p_values]
reject, pvals_corrected, _, _ = multipletests(p_vals, alpha=0.05, method='fdr_bh')

# Visualization of gene expression levels using a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='PAM50Call_RNAseq', y=gene_of_interest, data=df)
plt.title(f'Expression of {gene_of_interest} Across PAM50 Subtypes')
plt.ylabel('Expression Level')
plt.xlabel('PAM50 Subtype')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()