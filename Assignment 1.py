import matplotlib.pyplot as plt

# Assigning parameters
k = 0.1
A = 1
d = 0.1
T_e = 300
T_0 = 500
dt = 0.01
t_final = 100
dQ_0 = 0

# Determining the rate of heat loss
# dQ/dt = q
q = k * A * ((T_0 - T_e) / d)

# creating a list as a container for temperatures
temps = [T_0]
# creating a storage for the heat absorbed
heat = [dQ_0]

no_of_simulations = int(t_final / dt)
counts = 1
while counts <= no_of_simulations:
    dQ = q * dt * counts
    heat.append(dQ)

    T = -(T_0 - ((q * counts) / (A * k)))
    temps.append(T)
    print("For heat of {joule} J, the temperature {celsius}K".format(joule=dQ, celsius=T))
    counts += 1

    
# plotting the graph
plt.plot(dQ, T)
plt.xlabel('Heat')
plt.ylabel("Temperature")
plt.title("A Graph of Temperature Against Heat")
plt.show()