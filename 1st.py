import socket
print("----------------------------------------")
print("The program have service will help you\nselect one of service by input the number\n"
      "(1)find the website ip\n(2)find the ip host\n(3)find port number \n(4)find number port\n(q)exit\n")
print("----------------------------------------")
while True:
    try:
        select = input("Enter the number of service: ")
        if select == '1':
            website = input("Enter The website: ")
            ip = socket.gethostbyname(website)
            print(f"The ip of {website} is {ip}")
        elif select == '2':
            website_ip = input("Enter The ip: ")
            host = socket.gethostbyaddr(website_ip)
            print(f"This {website_ip} for this host {host[0]}")
        elif select == '3':
            port = input("Enter The port name : ")
            port_num = socket.getservbyname(port)
            print(f"The number of the port {port} is {port_num}")
        elif select == '4':
            num_port = int(input("Enter The port number : "))
            port_name = socket.getservbyport(num_port)
            print(f"The name of the port {num_port} is {port_name}")
        elif select.lower() == 'q':
            break
    except Exception:
        print("There is error!!, try again")
        continue
print("Exit program")
