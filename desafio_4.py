tot_faturamento_sp = 67836.43
tot_faturamento_rj = 36678.66
tot_faturamento_mg = 29229.88
tot_faturamento_es = 27165.48
tot_faturamento_outros = 19849.53 

faturamento_tot = (tot_faturamento_sp + tot_faturamento_rj + tot_faturamento_mg + tot_faturamento_es + tot_faturamento_outros)

percentual_sp = (tot_faturamento_sp / faturamento_tot)*100
percentual_rj = (tot_faturamento_rj / faturamento_tot)*100
percentual_mg = (tot_faturamento_mg / faturamento_tot)*100
percentual_es = (tot_faturamento_es / faturamento_tot)*100
percentual_outros = (tot_faturamento_outros / faturamento_tot)*100

print(f"percentual SP: {percentual_sp:.2f}%")
print(f"percentual RJ: {percentual_rj:.2f}%")
print(f"percentual MG: {percentual_mg:.2f}%")
print(f"percentual ES: {percentual_es:.2f}%")
print(f"percentual outros: {percentual_outros:.2f}%")