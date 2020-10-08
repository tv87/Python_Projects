import college_directory
myCollege = college_directory.CollegeDirectory("Hawthorne")
myCollege.addStudent("Hester Prynne", "hprynne@hawthrone.edu")
myCollege.addStudent("Rodger Chillingworth", "rchillingworth@hawthrone.edu")
print(myCollege.getEmailList())
