import speedtest  
  
  
st = speedtest.Speedtest()
  
option = int(input('''What speed do you want to test:  
  
1) Download Speed  
  
2) Upload Speed  
  
3) Ping 
  
Your Choice: '''))
  
  
if option == 1:  
  
    print("Download Speed: {:5.2f} Mbps".format(st.download()/(1024*1024)))  
  
elif option == 2: 
  
    print(st.upload())  
  
elif option == 3:  
  
    servernames =[]  
  
    st.get_servers(servernames)  
  
    print(st.results.ping)  
  
else:
  
    print("Please enter the correct choice !") 