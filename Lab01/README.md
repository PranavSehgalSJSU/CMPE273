# CMPE 273 – Week 1 Lab 1: Your First Distributed System (Starter)

This starter provides two implementation tracks:
- `python-http/` (Flask + requests) (CHOSEN PATH)
- `go-http/` (net/http)

Pick **one** track for Week 1.

### Lab Goal
Build **two services** that communicate over the network:
- **Service A** (port 8080): `/health`, `/echo?msg=...`
- **Service B** (port 8081): `/health`, `/call-echo?msg=...` calls Service A

Minimum requirements:
- Two independent processes
- HTTP (or gRPC if you choose stretch)
- Basic logging per request (service name, endpoint, status, latency)
- Timeout handling in Service B
- Demonstrate independent failure (stop A; B returns 503 and logs error)

## Deliverables
## 1. Repo link : 
      https://github.com/PranavSehgalSJSU/CMPE273/tree/main/Lab01
## 2. README updates:
   # how to run locally
      The code can be run locally by cloning git repository via :
         git clone https://github.com/PranavSehgalSJSU/CMPE273.git
      then opening folder in 2 seperate terminals and running:
         **python CMPE273\Lab01\python-http\service-a\app.py**
         **python CMPE273\Lab01\python-http\service-b\app.py**
   # success + failure proof (curl output or screenshot)
      Terminal outputs:
![Terminal_Output_A](./imgs/TerminalOutputs_A.png)
![Terminal_Output_B](./imgs/TerminalOutputs_B.png)

      Service Healths:
![Service_A_Health](./imgs/ServiceA_Health.png)
![Service_B_Health](./imgs/ServiceB_Health.png)
      
      Service Echos(Both Running):
![Service_A_Echo1](./imgs/HelloFromA1.png)
![Service_B_Echo1](./imgs/HelloFromB1.png)
      
      Service Echos(Only B Running):
![Service_A_Echo2](./imgs/HelloFromA2.png)
![Service_B_Echo2](./imgs/HelloFromB2.png)

   # 1 short paragraph: “What makes this distributed?”
