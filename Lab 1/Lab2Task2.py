st_hours = 9
st_mins = 30
sect1_dist = 2.5
sect1_speed = 10
sect2_dist = 3.0
sect2_speed = 12
sect3_dist = 4.0
sect3_speed = 15


sect2_time = sect2_dist/sect2_speed


start_time = st_hours + (st_mins / 60)  
sect1_time= sect1_dist/sect1_speed
run_time = sect1_time + sect2_time + sect3_time
end_time = start_time + run_time
end_time_hrs = int(end_time)
end_time_mins = int((end_time*60) % 60)
print("End time = " + str(end_time_hrs) + " hours " + str(end_time_mins) + " mins")