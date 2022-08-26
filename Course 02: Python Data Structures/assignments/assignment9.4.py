'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1
        
person_most_sent_mail = None
most_sent_mail_count = None

for person,mail_count in count.items():
    if most_sent_mail_count is None or most_sent_mail_count < mail_count:
        person_most_sent_mail = person
        most_sent_mail_count = mail_count
        
print(person_most_sent_mail, most_sent_mail_count)
