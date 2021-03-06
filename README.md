# Vending-machine
Programming a vending machine at a grocery store.

## About this project
A small grocery store with 3 main product lines: Seafood (HS), Meat (TH) and Vegetables (RC).
 - For Seafood, you have 3 types: Shrimp, Crab, Fish. The prices are 200, 500, and 60, respectively.
 - For Meat, you have 3 types: Chicken, Beef, Pork. Prices are 80, 120, and 100, respectively.
 - For Vegetables, you have 2 types: Potato, Corn. Prices are 10, 18, respectively.

Let's write an application that includes:
A. 3 functions for each product line (eg function haisan(), thit(), rau(), with the following functions:
- Select product type
- Choose quantity
- Select more product type and quantity (or enter 'exit' to exit)
- Calculate the total price for that product line and return the variables (variables) for each product line
- If the buyer chooses incorrectly -> Notification of incorrect selection and allows to choose again (or enter 'exit' to exit)

B. 1 large function contains all 3 functions above, has the following functions:
- Buyer can select product line -> activate a function in part A corresponding to selected product line
- Save the returned results into the corresponding variables
- After the buyer exits the function in part A, continue to ask the buyer if he wants to choose any more product lines
- If yes: continue to activate the function corresponding to the selected product line
- Repeat the above steps until the buyer enters 'finish' to exit
- Otherwise: the buyer enters 'finish' to exit the app

## Output
- Print out the price, quantity, and total price of the item the buyer has selected
- Print out the total price of the order
- For buyers to choose one of 3 payment options: "TienMat", "TheTinDung", "ViDienTu"
- If it is "TienMat"(cash): write a line "paid" and thank the buyer -> Exit the application

 - If "TheTinDung" (credit card):
 - Ask the user to enter a credit card number (requires 16 digits)
 - Check the length of the entered card number:
 - If longer or shorter than 16 digits: incorrect, ask to re-enter
 - If 16 digits are correct: write a line "paid" and thank the buyer -> Exit the application

 - If it is "ViDienTu" (e-wallet):
 - Ask the user to enter the e-wallet code (requires 9 digits)
 - Check the length of the entered card number:
 - If longer or shorter than 9 digits: incorrect, ask to re-enter
 - If 9 digits are correct: write a line "paid" and thank the buyer -> Exit the application
 - If not all 3 payment methods above: incorrect, ask to re-enter  
