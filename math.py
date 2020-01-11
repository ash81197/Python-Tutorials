import math

signal_power=int(input("Enter the signal power"))
noise_power=(int(input("Enter the noise power")))

ratio=signal_power/noise_power
decibels=10*math.log10(ratio)
print(decibels)

radians=3.15/2
height=math.sin(radians)
print(height)
