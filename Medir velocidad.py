#pip install speedtest-cli

import speedtest

st = speedtest.Speedtest()

d_st = st.download()

u_st = st.upload()

#Comprobar Ping 
st.get_servers([])
ping = st.results.ping

#Mostramos el resultado
print("Your Ping is", ping)

print("Tu velocidad de descarga es", d_st) 
print("Tu velocidad de subida es", u_st)

