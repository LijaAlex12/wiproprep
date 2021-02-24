# passenger and ticket
class Passenger:
  def __init__(self,name,age,distance):
    self.name=name
    self.age=age
    self.distance=distance
  def calculateTicketFare(self,passengerlist,fareperkilo):
    sum1=0
    ticketwithtax=0
    totalforall=0
    for i in range(n):
      ticketwithouttax=(passengerlist[i].distance*fareperkilo)
      if passengerlist[i].age>=60 or passengerlist[i].age<12:
        tax=0
      elif passengerlist[i].age>21 or passengerlist[i].age<59:
        tax=0.12*ticketwithouttax
      elif passengerlist[i].age>=12 and passengerlist[i].age<20:
        tax=0.1*ticketwithouttax
      nettaxperperson=ticketwithouttax*tax
      totalforall=totalforall+nettaxperperson
    return totalforall
  
  def countSeniorJuniorPassenger(self,passengerlist):
    cs=0
    cj=0
    for i in range(n):
      if passengerlist[i].age>=60:
        cs=cs+1
      elif passengerlist[i].age<12:
        cj=cj+1
    return cs+cj
  
listofpassengerobjects=[]
global n
n=int(input())

for i in range(n):
  name=input()
  age=int(input())
  distance=float(input())
  p=Passenger(name,age,distance)
  listofpassengerobjects.append(p)
  
fareperkilo=float(input())
print(p.calculateTicketFare(listofpassengerobjects,fareperkilo))
print(p.countSeniorJuniorPassenger(listofpassengerobjects))

    
 

        
        
        
