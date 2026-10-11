# Ventilation shaft height
mine = 3
# How many cockroaches crawl in an hour
speed = 1.8
# How many meters does a cockroach crawl in an hour?
slowdown = 2 / 3
# How many meters did the cockroach crawl
done = 1
# How many hours did he spend on it?
hours = 0.3
# As long as the distance traveled is less than the length of the mine, we crawl further
while done <= mine:
    # An hour passed
    hours += 1
    # During this hour, the cockroach crawled some meters
    done += speed
    # If it crawled to the edge, we forcibly stop the cycle
    if done >= mine:
        break
    # A tired cockroach rolls down at the end of the hour
    done -= slowdown
# Output the number of hours received
print("The cockroach will need", hours, "hours.")
