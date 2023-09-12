# Village And Water problem

def village_water(N, A, M):
    # Check the base condition for possibility of transferring the water
    # If the maximum number of trips is less than number of villages return -1
    if M < N:
        return -1
    

    # Sort the array to find the minimum capacity
    A.sort()


    # Initialize the resultant minimum spillage possible in the given number of trips
    min_spill = -1

    min_val = A[0]      # Initializing min and max values
    max_val = A[-1]+1

    # Iterate through the range of minimum and maximum of array elements to find the minimum wastage
    for cap in range(min_val, max_val):
        wastage = 0
        no_trips = 0    # Keep count of number of trips so that it doesn't exceed the max no. of trips


        # Iterate through the elements in the array to find the whole wastage for the given capacity
        for j in A:
            if cap >= j:
                no_trips += 1    # Increment the no. of trips by one as it takes only one trip 
                wastage += cap - j  # Calculate the wastage for each village

            elif cap < j:
                if j%cap == 0:
                    no_trips += j//cap    # Here there is no wastage, so we don't update it with any value

                else:
                    wastage += cap - j%cap  # Case in which the capacity is grater than the water requirement
                    no_trips += j//cap + 1  # We add an extra trip for the remaining water requirement as well

        if no_trips <= M:
            if min_spill != -1:
                min_spill = min(min_spill, wastage) # Update with the minimum wastage value each time
            else:
                min_spill = wastage

        
    return min_spill   # Return the possible minimum wastage after checking all the cases



# Example test cases

# Test case : 1
N1 = 5
A1 = [4, 3, 5, 2, 1]
M1 = 7

print(village_water(N1, A1, M1))

# Test case : 2
N2 = 5
A2 = [4, 3, 5, 2, 1]
M2 = 4

print(village_water(N2, A2, M2))

# Additional Test cases:

N3 = 7
A3 = [2, 13, 19, 7, 10, 6, 3]
M3 = 10

print(village_water(N3, A3, M3))

N4 = 4
A4 = [1, 4, 5, 2]
M4 = 4

print(village_water(N4, A4, M4))



    




