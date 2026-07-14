# 💰 Loan EMI Calculator (Python)

A simple Python-based Loan EMI Calculator that helps users calculate their monthly loan installment (EMI), total payment, and total interest based on the loan amount, annual interest rate, and loan tenure.

## 📌 Features

- Calculate Monthly EMI
- Calculate Total Amount Payable
- Calculate Total Interest Payable
- User-friendly command-line interface
- Input validation for better user experience
- Fast and lightweight

## 🛠️ Technologies Used

- Python 3.x
- Math Module

## 📂 Project Structure

```
Loan-EMI-Calculator/
│
├── loan_emi_calculator.py
├── README.md
└── screenshots/
    └── output.png (optional)
```

## 📐 EMI Formula

The EMI is calculated using the standard formula:

```
EMI = [P × R × (1 + R)^N] / [(1 + R)^N − 1]
```

Where:

- **P** = Loan Amount
- **R** = Monthly Interest Rate (Annual Rate ÷ 12 ÷ 100)
- **N** = Loan Tenure in Months

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Loan-EMI-Calculator.git
```

2. Navigate to the project folder

```bash
cd Loan-EMI-Calculator
```

3. Run the program

```bash
python loan_emi_calculator.py
```

## 💻 Sample Output

```
========= Loan EMI Calculator =========

Enter Loan Amount: 500000
Enter Annual Interest Rate (%): 8.5
Enter Loan Tenure (Years): 5

Monthly EMI        : ₹10,258.74
Total Payment      : ₹615,524.40
Total Interest     : ₹115,524.40
```

## 🚀 Future Improvements

- GUI using Tkinter
- EMI Payment Schedule
- Loan Comparison Feature
- Export EMI Report to PDF
- Graphical Charts using Matplotlib

## 🎯 Learning Outcomes

This project helped in understanding:

- Functions in Python
- Mathematical calculations
- User input handling
- Conditional statements
- Code organization
- Financial calculations

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Om Tiwari**

- GitHub: https://github.com/Omtiwari-prog
