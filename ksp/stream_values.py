import krpc
from time import sleep
conn = krpc.connect()
vessel = conn.space_center.active_vessel
flight_info = vessel.flight()
altitude = conn.add_stream(getattr, flight_info, 'mean_altitude')
gforce = conn.add_stream(getattr, flight_info, 'g_force')
speed=conn.add_stream(getattr, flight_info, 'speed')
longitude=conn.add_stream(getattr, flight_info, 'longitude')
latitude=conn.add_stream(getattr, flight_info, 'latitude')
velocity=conn.add_stream(getattr, flight_info, 'velocity')
hspeed=conn.add_stream(getattr, flight_info, 'horizontal_speed')
vspeed=conn.add_stream(getattr, flight_info, 'vertical_speed')
rotation=conn.add_stream(getattr, flight_info, 'rotation')
adensity=conn.add_stream(getattr, flight_info, 'atmosphere_density')
aero=conn.add_stream(getattr, flight_info, 'aerodynamic_force')
tv=conn.add_stream(getattr, flight_info, 'terminal_velocity')
airspeed=conn.add_stream(getattr, flight_info, 'equivalent_air_speed')
vs=conn.add_stream(getattr, flight_info, 'vertical_speed')
lift=conn.add_stream(getattr, flight_info, 'lift')
drag=conn.add_stream(getattr, flight_info, 'drag')
tas=conn.add_stream(getattr, flight_info, 'true_air_speed')

#ref https://krpc.github.io/krpc/python/api/space-center/flight.html
while True:
    print("alt", altitude())
    print("force", gforce())
    #print("speed", speed())
    #print("velocity", velocity())
    print("latitude",latitude())
    print("longitude",longitude())
    #print("vspeed", vspeed())
    #print("hspeed", hspeed())
    print("rotation", rotation())
    print("atmospheric density", adensity())
    print("aerodynamic_force", aero())
    print("terminal velocity", tv())
    print("air speed", airspeed())
    print("vertical speed", vs())
    print("lift", lift())
    print("drag", drag())
    print("true air speed", tas())


    sleep(1.0)
