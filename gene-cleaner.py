import pandas as pd

# SHOW ME THE PATH
file_path = 'data/here_be_file.csv'

df = pd.DataFrame(pd.read_csv(file_path, sep=';', on_bad_lines='warn'))

# Extracting Gene ID
# Soltu.DM.01G000790.1 ==> 01G000790
df['gene_id'] = df['transcript_id'].apply(lambda x: x.split('.')[2:-1][0])

# DataFrames for processed and rejected data
processed_data = []
rejected_data = []

# Track accepted transcript_ids by main id and PValue
accepted_ids = {}

# BUCKLE UP! WE GOING IN!
for index, row in df.iterrows():
    #Define columns of interest
    pvalue = row['PValue_pe_soltub']
    main_id = row['gene_id']

    # Chek if we already processed the ID
    if(main_id, pvalue) in accepted_ids:
        # Reject that gene ID with that PValue been acceped erlier
        rejected_id = accepted_ids[(main_id, pvalue)]
        
        #stating reasons to reject
        rejection_reason = f"Duplicate PValue {pvalue} for Gene ID: {main_id}"
        row['rejection_reason'] = rejection_reason
        #saving rejected data, control
        rejected_data.append(row.to_dict())
    else:
        # Accept this row and mark this main_id with this PValue as accepted
        processed_data.append(row.to_dict())
        accepted_ids[(main_id, pvalue)] = row['transcript_id']


processed_df = pd.DataFrame(processed_data)
rejected_df = pd.DataFrame(rejected_data)

# Drop the auxiliary 'gene_id' column
processed_df.drop(columns=['gene_id'], inplace=True)
rejected_df.drop(columns=['gene_id'], inplace=True)


#Saving results to file
rejected_df.to_csv('rejected_data.csv')
processed_df.to_csv('cleaned_data.csv')


