# The triathlon consists of swimming, cylcing and running
# The completion time per activity needs to be entered byser
swimming = int(input("Please enter the completion time of swimming: "))
cycling = int(input("Please enter the completion time of cycling: "))
running = int(input("Please enter the completion time of running: "))

# the sum of the three variables above determines the total completion time
total_triathlon = swimming + cycling +running
print(total_triathlon)  

# below statements show criteria to win which award
# Provincial award when total time is between 0 and 100
if (total_triathlon > 0) and (total_triathlon <=100): 
    print("You have won a Provincial Colours award!")
# Provincial half colours award when total time is between 101 and 105
elif (total_triathlon >=101) and (total_triathlon <=105): 
    print("You have won a Provincial Half Colours award!")
# Provincial scroll award when total time is between 106 and 110
elif (total_triathlon >= 106) and (total_triathlon <=110): 
    print("You have won a Provincial Scroll award!")
# No award when total time is 111 or above
elif (total_triathlon >= 111):
    print("Sorry, you have not won an award.")
