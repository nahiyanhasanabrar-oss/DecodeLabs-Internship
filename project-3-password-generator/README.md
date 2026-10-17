# 🔐 Enterprise Password Generator (CLI)

An enterprise-grade, cryptographically secure Command Line Interface (CLI) Random Password Generator built using Python. This tool uses Python's built-in `secrets` module instead of `random` to guarantee unpredictable password generation and utilizes `.join()` for optimal linear time complexity $O(N)$.

---

## 🌟 Key Features

* **Cryptographically Secure:** Powered by the standard `secrets` module (`secrets.choice()`) for maximum entropy and defense against prediction attacks.
* **Linear Time Complexity $O(N)$:** Optimized memory performance using standard string joining instead of quadratic string concatenation.
* **Standard Character Sets:** Uses standard `string.ascii_letters`, `string.digits`, and `string.punctuation` pools for secure password composition.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Version Control:** Git & GitHub

---

## 🚀 How to Run

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/nahiyanhasanabrar-oss/DecodeLabs-Internship.git](https://github.com/nahiyanhasanabrar-oss/DecodeLabs-Internship.git)
