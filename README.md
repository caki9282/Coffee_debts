# Coffee_debts
Welcome to Coffee Debts!

Context: Bob, Jeremy, and the other 5 coworkers in the Bertram Labs office love coffee. In fact, everyday, right after lunch, they walk down the street to their favorite coffee shop to grab a cup to go. Bob always gets a cappuccino, Jeremy likes his coffee black, and the others have their favorite coffee beverage too. To ease the checkout process, only one coworker pays for all the coffees each day. As you can imagine, they have a problem every day: who's turn is it to pay for coffee?

Problem statement: Write a software program to help coworkers decide who should pay for coffee. Consider that not all drinks cost the same, so to be fair please take this into account when crafting your solution.

Solution: My solution to this problem was to create a program that would have a database of Users that keeps track of the user's name and their total debt. The total debt was created by the cost of the coffee they had bought. The program would then find who has the most debt (i.e they have been buying the more expensive coffee more often) and have them pay for that week's coffee total among coworkers. Once the week's buyer buys the coffee their overall debt will be reduced by the total price excluding their coffee price, But the other coworkers that didn't pay their debt would increase by their cost of coffee. This would repeat with the program choosing whoever has the highest debt to buy the coffee the next week, and the next week, and so forth.

Assumptions made:
- Someone has a receipt of all the coffee orders
- each person knows their coffee amount
- tax is not a factor to worry about
- A coworker can pay multiple weeks in a row.
--------------------------------Data------------------------------------------
Pre-Existing Accounts (data):
User: Calvin (admin)
Username: Calvin
Password: Ck10940897

User: Allie
Username: Allie
Password: albu1234

User: boblee
Username: boblee
Password: boba1234

User: billy
Username: billy
Password: biki1234

User: Suchi
Username: Suchi
Password: sushi123
---------------------How to build and run the solution---------------------------
How to build and run the program:
- Make sure Django is installed:
  - if Django is not installed then follow this guide to install it.
    - Windows:
      - https://docs.djangoproject.com/en/5.0/howto/windows/
    - Mac:
      - https://docs.djangoproject.com/en/5.0/topics/install/
- Open a new terminal
- Clone the GitHub repo into an IDE (Visual Studio Code is the one this program was created on)
  - git clone (HTTPS link)
- Once cloned navigate through the directory:
  - Bertram Code/coffee_debts/coffee_debts
  - cd Bertram, cd coffee_debts, cd coffee_debts
- Once in the above directory run the program using this line in the terminal:
  - python3 (or python depending on what python is installed on your local device) manage.py runserver
  - i.e python3 manage.py runserver
- Once the program has begun running open a browser
- in the search bar type your localhost: either work
  - "your local ip:8000"/debts/login/
  - "your local ip:8000"/debts/register/
- Then you can either log in with a pre-existing account or register your own
- to access the admin page:
  - "your local ip:8000"/admin/
  - use user Calvin to log in to the admin page.
- Once you're done or want to switch accounts just click Logout in the top right corner!
  
--------------------------------Project Features-----------------------------------
Features:
- Home Page:
  - click the submit button to show the cost-fillable area
  - Put any amount you want in there that amount will be added to the debt of the current user you are logged in to.
- Debts Page:
  - The Debts page shows the debt of every user in the program 
- Who, Pays? Page:
  - Takes every single user in the system and has an input of cost, which takes the cost of each person's coffee (hence why I assumed they knew or had a receipt) and then updates the buyer's debt subtracted from every other person's coffee total and everyone else's coffee cost get added to their total debts.
  - Then prompts you who has paid this week and that everyone else debt has been updated.



