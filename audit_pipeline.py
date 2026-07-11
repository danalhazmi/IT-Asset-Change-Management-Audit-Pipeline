import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean visualization style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = [12, 7]

print("🛡️ Generating Deep-Detail IT Audit Visualizations...\n")

data_file = 'it_audit_logs.csv'

if os.path.exists(data_file):
    df = pd.read_csv(data_file)
    df.columns = df.columns.str.strip()
    
    # 1. Governance Audit Risk Scoring
    criticality_map = {'Critical': 40, 'High': 30, 'Medium': 20, 'Low': 10}
    df['Base_Criticality_Score'] = df['System_Criticality'].map(criticality_map)
    df['UAT_Bypass_Penalty'] = df['Tested_In_UAT'].apply(lambda x: 25 if x == 'No' else 0)
    df['Approval_Void_Penalty'] = df['Approver_Role'].apply(lambda x: 35 if x == 'None' else (15 if x == 'Developer' else 0))
    df['Calculated_Risk_Score'] = df['Base_Criticality_Score'] + df['UAT_Bypass_Penalty'] + df['Approval_Void_Penalty']
    
    # 2. Plotting Graph 1 (Advanced Boxplot + Individual Event Points)
    plt.figure()
    order_list = ['Low', 'Medium', 'High', 'Critical']
    
    # Base Boxplot with transparency for professional layering
    sns.boxplot(
        x='System_Criticality', 
        y='Calculated_Risk_Score', 
        data=df, 
        order=order_list, 
        hue='System_Criticality',
        palette='Oranges',
        boxprops=dict(alpha=0.3),
        legend=False
    )
    
    # High-Density Layer: Adding every single change log as a distinct data point!
    sns.stripplot(
        x='System_Criticality', 
        y='Calculated_Risk_Score', 
        data=df, 
        order=order_list,
        hue='Execution_Window',
        palette='deep',
        size=7,
        jitter=0.2,
        linewidth=0.5,
        edgecolor='black'
    )
    
    plt.title('High-Density IT Risk Exposure Profile across Infrastructure Tiers', fontsize=14, pad=15, fontweight='bold')
    plt.xlabel('System Criticality Tier (Asset Classification)', fontsize=12)
    plt.ylabel('Calculated Audit Risk Score (Aggregated Deficiencies)', fontsize=12)
    plt.legend(title="Execution Window Type", loc="upper left")
    plt.tight_layout()
    
    # Save the detailed chart
    plt.savefig('advanced_it_audit_risk_profile.png', dpi=300)
    plt.close()
    
    print("💾 Success! Generated High-Density Asset: advanced_it_audit_risk_profile.png")
    print("✅ Run complete. Check the left sidebar for your new detailed visualization.")
else:
    print("❌ Error: Dataset file not found.") 