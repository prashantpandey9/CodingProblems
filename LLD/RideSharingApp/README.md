# Question

Design a ride sharing application where drivers can offer rides(origin, destination, no of seats), any rider can request rides(origin, destination, no of seats)

The program should take as input two or more drivers and a set of riders requesting rides multiple rides can happen simultaneously.


There is an algorithm to choose to calculate the ride amount changed for a given ride based on distance and no of seats.
1. When the ride closes, show the amount charged to the rider.
2. Ride amount if No of seats >= 2: No of kilometers * No of seats *0.75 * Amount charged per KM
3. Ride amount if No of seats = 1: No of kilometers * Amount Charged per KM 


Functions:
1. Register a driver/cab
2. Register a rider.
3. Book a ride
4. Create a ride
5. Generate bill.
6. Check the validity of an ongoing ride for a new rider
7. Update ride status
8. Fetch revenue of all the rides taken by driver/cab




Solution:

 - Assumptions:
 1. Amount charged per km = 10
 2. Source/destination are integer
 3. X and Y direction
 4. Driver update the status of the trip