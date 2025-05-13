# Stackulator

## Overview  
**Stackulator** is a stack-based calculator implemented to perform arithmetic operations and evaluate expressions in different notations such as **postfix**, **prefix**, and **infix**. It leverages stack data structures to handle mathematical computations effectively.

---

## Key Features  
- **Stack Implementation**:  
  The project uses a stack data structure to manage operands and operators, ensuring efficient and logical evaluation of expressions.
  
- **Expression Handling**:  
  - **Postfix (Reverse Polish Notation)**: Operands appear before operators (e.g., `3 4 +`).
  - **Prefix (Polish Notation)**: Operators appear before operands (e.g., `+ 3 4`).
  - **Infix (Standard Notation)**: Operators are placed between operands (e.g., `3 + 4`).

- **Error Handling**:  
  The code includes mechanisms to check for invalid expressions, mismatched parentheses, and divide-by-zero errors.

---

## How to Use  

1. Clone the repository:  
   ```bash
   git clone https://github.com/BehradShirkavand/Stackulator.git
   cd Stackulator
   ```

2. Run the program:  
   ```bash
   python gui.py
   ```

3. Input your expression and select the evaluation method (postfix, prefix, or infix).  
