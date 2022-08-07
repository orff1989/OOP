# Ex1 - OOP
 Or Finberg, 209163054

1.
    https://github.com/bernadinm/elevator 
    https://github.com/akirillov/elevator-scheduler 
    https://github.com/aspanu/ElevatorControl 
    
    In this project we will solve the problem of how to mange elvator control system with the knowing of all the future calls of every floor.
    
    # UML:
    
    ![diagram-5552862024406244954](https://user-images.githubusercontent.com/43110158/142610520-abcef666-65af-483c-ae68-61f9bbe23e3a.png)

	
	
# 2. The algorithm: 
		
		a. the algorithm will allocate the first elevator to the first call.
		
		b. we will calculate what time the elevator will reach to its destination.
		
		c. the algorithm will calculate the time it will reach to the source floor of every call with consideration
		   of the cuuret position of the elevator, and the end time of the elevator's last call.
		   
		d. if the elevator will get in time for the next call, we will assign this elevator to the new call.
		   and if it will not reach in time,  we will check every elevator and assign the elevator that will reach faster.
		
		
