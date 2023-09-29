# CS50 Python Final Project
    #### Video Demo:  https://youtu.be/5I5eSl1nyPo
    #### Description:
  
    
    
    
This documentation is about my CS50 Final Project. In this project. We’re going to receive a CSV file with the data of 10 new students of Hogwarts. This CSV file contains the name, characteristics and birthdate. Our task is to classify which houses they belong to according to the main characteristics and what are the grades according to their age. At the end, we’ll create a new CSV file that contains the new classifications. Depending on the characteristics that the person has in the CSV file, we’ll classify which house do they belong to. After some research, we define three main characteristics of each house. For the house Gryffindor, we have the words “Courage”, “Loyalty” and “Adventure”. For Hufflepuff, we have “Dedication”, “Patience” and “Honesty”. For Ravenclaw, we have “Wisdom”, “Creativity” and “Perfectionism” and finally for Slytherin, we have “Ambition”, “Competitive” and “Leadership”. For the grade, we assume that every person at Hogwarts will start at a certain grade according to their age. 

In the first step, you import the necessary libraries which include the 'sys’ and ‘csv’ library. SYS library is used for taking the command line arguments as inputs while the CSV library is used for working with the .csv files that is importing and exporting them.

The program comprises of three functions. The first function which is named as Check Correct Arguments counts the length of command line arguments. If it is less than 3, it displays too few arguments and displays too many arguments in case it is greater than 3. It exits the program if it is not a CSV file.

The second function namely Select_House returns the house name based on the passed characteristic. These characteristics for the respective house have been already explained. 

The third function returns the Grade in which the student will be inducted at the Hogwarts. This decision is made based on student’s age.

The main function is invoked at the end in which the CSV file namely new_students.csv is first read and then the functions select_house and select_grade are called to check the students house and grade. Finally, this new information is written into a new CSV file namely after.csv.


