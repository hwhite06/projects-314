import re

#First we will open the file, have it read through and store the data. 
log_entries = []
file = open("access.log")
data = file.readlines()

# Using this search we can filter out all of the log entries that were botpokes. 
# We can search specifically for "Botpoke" as all of the lines we want to target 
# will say this exactly. 
for x in data:
    if x.find("BotPoke") < 0:
        log_entries.append(x)

# after populating a new set with the log entries that we want, we can find the 
# amount of log entries. 
print("There are", len(log_entries), "log entries remaining.")


# We can then find a list of unique IP addresses using regular expressions again.
# This time we search for IP addresses that are identical and filter them out. 
match_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
unique_ip = set()

for x in log_entries:
    result = re.match(match_ip, x)
    if result:
        unique_ip.add(result[0])

print("The unique IP addresses in this log are:", unique_ip)