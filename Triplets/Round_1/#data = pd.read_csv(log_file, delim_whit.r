#data = pd.read_csv(log_file, delim_whitespace=True)
#data = data[data.Time != 'END'] #removes the end of round lines
#total_deaths = data[(data.CausaMortis == "fluor") | (data.CausaMortis == 'phosph') | (data.CausaMortis == 'nonrad')]

# Average lifetime calculator:
#def avg_lifetime(total_deaths):
#    #total_deaths = data[(data.CausaMortis == "fluor") | (data.CausaMortis == 'phosph') | (data.CausaMortis == 'nonrad')]
#    lifetime = total_deaths['Time'].to_numpy(float)
#    avg_life = np.mean(lifetime)
#    return avg_life
#
## Diffusion Length calculator:
#def ld_calculator(total_deaths):
#    #total_deaths = data[(data.CausaMortis == "fluor") | (data.CausaMortis == 'phosph') | (data.CausaMortis == 'nonrad')]
#    dx = total_deaths['DeltaX'].to_numpy(float)
#    dy = total_deaths['DeltaY'].to_numpy(float)
#    dz = total_deaths['DeltaZ'].to_numpy(float)
#    diffusion_length = np.sqrt(np.mean(dx**2+dy**2+dz**2))
#    return diffusion_length
#
#Ld  = ld_calculator(total_deaths)
#tau = avg_lifetime(total_deaths)
#print("Average lifetime is: ", "{:.2f}".format(tau), 'ps')
#print('Diffusion length is:', "{:.2f}".format(Ld), 'AA')

#avg
#dead

#data












#recria o que eu fazia no bash, preciso mudar a forma e usar o uniq nas colunas status (dead e converted)
#fluor_NPB  = dead[(dead.CausaMortis == "fluor") & (dead.Location == 0.0)]
#nonrad_NPB = dead[(dead.CausaMortis == "nonrad") & (dead.Location == 0.0)]
#ISC_NPB = data[(data.Status == "converted") & (data.CausaMortis == "isc") & (data.Location == 0.0)]
#rISC_NPB = data[(data.Status == "converted") & (data.CausaMortis == "risc") & (data.Location == 0.0)]
#
#print("Fluor NPB:",len(fluor_NPB)) #bash
#print("Nonrad NPB:",len(nonrad_NPB)) #bash
#print("ISC NPB:",len(ISC_NPB)) #bash
#print("rISC NPB:",len(rISC_NPB)) #bash
#print("--------------------------------------")
#
#fluor_DCJTB = dead[(dead.CausaMortis == "fluor") & (dead.Location == 1.0)]
#nonrad_DCJTB = dead[(dead.CausaMortis == "nonrad") & (dead.Location == 1.0)]
#ISC_DCJTB = data[(data.Status == "converted") & (data.CausaMortis == "isc") & (data.Location == 1.0)]
#rISC_DCJTB = data[(data.Status == "converted") & (data.CausaMortis == "risc") & (data.Location == 1.0)]
#print("Fluor DCJTB:",len(fluor_DCJTB)) #bash
#print("Nonrad DCJTB:",len(nonrad_DCJTB)) #bash
#print("ISC DCJTB:",len(ISC_DCJTB)) #bash
#print("rISC DCJTB:",len(rISC_DCJTB)) #bash
#print("--------------------------------------")
#
#TTS_NPB_NPB = data[(data.Status == "converted") & (data.CausaMortis == "tts") & (data.Location == 0.0)]
#TTS_NPB_DCJTB = data[(data.Status == "converted") & (data.CausaMortis == "tts") & (data.Location == 1.0)]
#print("TTS NPB p/ NPB:", len(TTS_NPB_NPB))
#print("TTS NPB p/ DCJTB:", len(TTS_NPB_DCJTB))