# Pairing Mentors and Mentees script

This script is written to give a suggested list of students for each mentor. 

Mentees' and Mentors' area of interest are inputted using the csv files from microsoft forms they submitted, and the script aims to group participants according to their areas of interests. 

A risk averse approach is used because: 
<ol>
<li>it is too time consuming to find the best combination</li>
<li>groupings are made according to students who rank mentor's area of interest as more preferred 
eg. here is an example of students' preferences with lower scores meaning more preferred {mentor: {'Pemika': 17, 'Benjamin': 17, 'Shenoli': 18, 'Steven': 18, 'Nicholas': 19, 'Tina': 19, 'Nina': 19, 'haodong': 19, 'Sandhyaa': 19, 'Jarod': 19, 'Mohnish': 20, 'Olga': 21, 'Tra My': 21, 'Xiaojiao ': 21, 'Yee Mei': 22, 'Hung': 23, 'Archibold ': 25}}. In this case, Pemika, Benjamin, and Shenoli would be grouped to the mentor's group. </li>
<li>bias: ordering of data affects grouping ie. the mentors with names who appear first in data likely to get their preferred mentees first</li>
</ol>

## duplicate rank issue

in case of "Hung" and "haodong" there are rankings missing due to duplicate rank
So, their rankings were modified 
eg. ranking duplicate = 1, one of them modified to 2 



