# Tennis shop parser
The script can be modified for your tasks, include any stores and product categories in parsing.
![image](https://user-images.githubusercontent.com/105886632/171841535-12b6bb9c-ce1d-4463-bfff-7ccef6ac34a8.png)

## Technology stack
- Python
- Beautiful Soup 4
- Pandas

## Author
AlexDoved

## How to use the program
1. git clone https://github.com/AlexDoved/tennis_shops_parser.git
2. python -m venv venv
3. source venv/Scripts/activate
4. python -m pip install --upgrade pip
5. pip install -r requirements.txt
6. python main.py

## Example of using the program
After running the script, the user is prompted to select a tennis store from the suggested list.
If the parser for the selected store has not yet been implemented, the user will receive a message about it.
![image](https://user-images.githubusercontent.com/105886632/171835617-73f730a9-61d8-4182-9066-a1b30cec90da.png)
It's the same with product categories and sports equipment brands or clothing brands.
![image](https://user-images.githubusercontent.com/105886632/171836827-610811c2-68ab-4b95-a12b-d322f0895a57.png)
At the moment, the program works for the Racketlon store -> rackets category -> Wilson and Babolat brands
![image](https://user-images.githubusercontent.com/105886632/171837417-052fbfc6-2a18-4128-8853-8ea916c65fbb.png)
The program outputs the result in the form of names of rackets, links to rackets in the store and prices for rackets.
After the output of the result, the program offers to save the results to an Excel spreadsheet.
![image](https://user-images.githubusercontent.com/105886632/171837906-8c3e0c31-a373-4ff6-b6fd-614770797e19.png)
If the tables folder is not created, it is automatically created when saving the results to an Excel spreadsheet.

![image](https://user-images.githubusercontent.com/105886632/171838385-3779da90-78b5-4cf7-81dc-7b6d47bcf23a.png)

The files are named according to the rule: brand_category.xlsx
  
![image](https://user-images.githubusercontent.com/105886632/171839634-77f07363-3358-4452-9751-7feb4c7d439d.png)

An Excel spreadsheet with the results looks like this:

![image](https://user-images.githubusercontent.com/105886632/171838605-82d45939-57be-4c98-b54a-16fc9439f095.png)









