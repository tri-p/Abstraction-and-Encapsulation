# Abstraction-and-Encapsulation
Three different programs created in Python that used abstraction and encapsulation in the process.

## Fan program
A program that uses getter and setter methods to know the attributes of the fan.

### To run the program
1. Open the file.
2. Run the Python code 'test_fan.py'.
3. It will show the default values and details about a fan.
4. It will show the changed details for fan 1.
5. It will show the changed details for fan 2.

### Sample output
```
DEFAULT FAN
Speed: SLOW 
The fan is off 
Radius: 5.0 
Color: Blue

FAN 1
Speed: FAST 
The fan is on 
Radius: 10.0 
Color: Yellow

FAN 2
Speed: MEDIUM 
The fan is off 
Radius: 5.0 
Color: Blue
```

## Car program
A program that uses getter method that shows the model of a car with a default speed of 0. It calls the "accelerate" five times adding 5 to the speed each time the method is called. It also calls the "brake" five times, subtracting 5 from the speed each time the method is called.

### To run the program
1. Open the file.
2. Run the Python code 'test_car.py'.
3. It will show the model of the car.
4. It will show the speed gets higher as it is called five times.
5. It will show the speed get lower as it is called five times.

### Sample Output
```
Year Model: 1993
Make: Chevrolet
Speed: 0

=====

The car is accelerating...
Current Speed: 5
Current Speed: 10
Current Speed: 15
Current Speed: 20
Current Speed: 25

Year Model: 1993
Make: Chevrolet
Speed: 25

=====

The car is braking...
Current Speed: 20
Current Speed: 15
Current Speed: 10
Current Speed: 5
Current Speed: 0

Year Model: 1993
Make: Chevrolet
Speed: 0

```

## Pet program
A program that uses getter and setter methods to prompt the user for pet information. The output is to display the pet information.

### To run the program
1. Open the file.
2. Run the Python code 'test_pet.py'.
3. It will ask the user for the pet's name, animal type, and age.
4. It will display the pet's information.

### Sample Output
```
What is the pet's name? Yumi
What type of animal is the pet? Dog
What is the pet's age? 4

=====

PET'S INFORMATION
Name: Yumi 
Animal Type: Dog 
Age: 4
```
