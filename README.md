[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9apGZMRE)
# Motor Test
In this assignment, you'll test the Pico board, the motor driver board and the DC motors.
  
## Requirements:
Complete the Python scripts and answer the questions by editing the [README](/README.md) file. 
### (50%) [ramp_up_down.py](/ramp_up_down.py)
Slowly increase and decrease both motors' speed. Both motors should take actions at the same time.
1. (10%) Ramp up both motors' speed (from stall to max) in 4 seconds. Spin both motors **forward**.
2. (10%) Slow down both motors' speed (from max to stall) in 4 seconds. Spin both motors **forward**.
3. (10%) Ramp up both motors' speed (from stall to max) in 4 seconds. Spin both motors **backward**.
4. (10%) Slow down both motors' speed (from max to stall) in 4 seconds. Spin both motors **backward**.
5. (10%) Stop both motors.
> **Hint**:
> - you may want to refer to the `fade_in_fade_out.py` from your second assignment.
> - No loop is needed.

### (50%) Estimate Motor Speed
Make marks on both wheels at same spot before you start the testing [script](/estimate_speed.py). Run testing script and observe the motors behaviors carefully.
1. (10%) Complete the testing script: [estimate_speed.py](/estimate_speed.py). Spin both motors on same direction with 50% duty cycle PWM signals. Let the spinning last for 1 minute. Then stop.
> **Hint**: No loop is needed.
2. (30%) Observe the motor's behavior carefully and answer the questions below.
   1. (20%) Can you estimate the speed of each motor using "revolutions per minute (RPM)"? Please round the RPM to **one decimal place**. 
      > Your answer here.
   2. (10%) What would be the reasons if the speeds of the motors were different? 
      > Your answer here.
3. (10%) Upload images to show final location of the marks on each wheel. 
   
## AI Usage Policy
Please give credits to your AI assistance. Refer to the [syllabus](https://linzhanguca.github.io/_docs/robotics1-2024/syllabus.pdf) for the citation format.
