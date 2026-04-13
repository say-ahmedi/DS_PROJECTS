

### Phase 1: Create the Foundation

Open a blank Excel workbook and create exactly five distinct sheets (tabs) at the bottom. Name them as follows:

1. **📊 Dashboard** (Your Command Center)
2. **💸 Master Ledger** (Where all transactions are logged)
3. **🏢 Business Operations** (Your business firewall)
4. **⚖️ Qard al-Hasan** (Debt & Receivables)
5. **🥇 Halal Wealth & Zakat** (Investments and Purification)

---

### Phase 2: Build the "Master Ledger" (Sheet 2)

This is the engine of your entire system. Instead of having separate sheets for income and expenses, put everything here.

1. Create these exact column headers across row 1 (A through G):
   * **Date**
   * **Transaction Type** (Income, Expense, or Transfer)
   * **Category** (Needs, Wants, Halal Wealth, Biz Expense)
   * **Description** (e.g., Magnum Groceries, Yandex)
   * **Account Used** (Kaspi Personal, Kaspi Business, Halyk EF, Visa Rewards, Investment Card)
   * **Destination Account** (Only use this if the Type is "Transfer")
   * **Amount (₸)**
2. **The Transfer Rule:** When moving money to your Halyk Emergency Fund, log it as a "Transfer" in column B, put "Kaspi Personal" in Account Used, and "Halyk EF" in Destination Account. This prevents the spreadsheet from thinking you lost money.

---

### Phase 3: Build the "Dashboard" (Sheet 1)

This sheet will act as your daily snapshot. It will read the data from your Master Ledger.

**Section 1: Net Worth Snapshot**

1. List your five accounts vertically.
2. Next to each account, use a `SUMIFS` formula to calculate the balance. For Kaspi Personal, the logic is: *Total Income to Kaspi Personal MINUS Total Expenses from Kaspi Personal MINUS Transfers out of Kaspi Personal PLUS Transfers into Kaspi Personal.*
3. Create a "Total Net Worth" cell that sums all five accounts.

**Section 2: The 50/30/20 Budget Engine**

1. Create a cell for  **Monthly Personal Income** . (This is where you manually type the salary/draw you take from your business + your scholarship).
2. Create three rows below it:
   * **🛒 Needs (50%)** -> Formula: `Monthly Income * 0.50`
   * **🎮 Wants (30%)** -> Formula: `Monthly Income * 0.30`
   * **💰 Wealth/Debt (20%)** -> Formula: `Monthly Income * 0.20`
3. Next to those targets, create an **"Actual Spent"** column. Use a `SUMIFS` formula here to pull the total spent for the current month from your Master Ledger based on the Category (Needs, Wants, etc.).

---

### Phase 4: Build the "Business Operations" (Sheet 3)

This is your firewall. Personal money and business money must never mix here.

1. **Gross Revenue Section:** Use a `SUMIFS` formula to total all "Income" logged in the Master Ledger where the Account Used is "Kaspi Business".
2. **Business Expenses Section:** Use a `SUMIFS` formula to total all "Expenses" logged where the Account Used is "Kaspi Business" (e.g., IT, Marketing, Taxes).
3. **Net Profit:** Subtract Expenses from Gross Revenue.
4. **Owner's Draw:** Manually record the amount you transfer from Kaspi Business to Kaspi Personal to fund your 50/30/20 Dashboard.

---

### Phase 5: Build the "Qard al-Hasan" Tracker (Sheet 4)

This tracks your 0% interest obligations.

**Section 1: My Debts**

1. Total Debt Amount: 400,000 ₸.
2. Target Payoff Date.
3. Total Paid So Far: Use a `SUMIFS` formula to sum all expenses in your Master Ledger categorized as "Debt Repayment."
4. Remaining Balance:  *Total Debt - Total Paid So Far* .
5. Required Monthly Payment:  *Remaining Balance / Months Remaining* .

**Section 2: Receivables (Money owed to you)**

1. Create columns: Name, Original Loan Amount, Paid Back So Far, Remaining Balance, Deadline.
2. When a friend pays you back, log it in your Master Ledger as a "Transfer" so it safely enters your Kaspi or Halyk account without messing up your personal income taxes or 50/30/20 budget.

---

### Phase 6: Build "Halal Wealth & Zakat" (Sheet 5)

This is for long-term growth and spiritual purification.

**Section 1: Assets**

1. **Halyk Emergency Fund:** Pull the current balance from your Dashboard. Set a target cell (e.g., 100,000 ₸) and create a percentage progress formula.
2. **Gold & Equities:** Create columns for Asset Name, Grams/Shares Owned, Average Buy Price, and Current Market Value.

**Section 2: Zakat Calculator**

1. Create a "Total Zakatable Wealth" cell. This formula should add your liquid cash (Kaspi Personal + Halyk + Visa Rewards + Investment Card cash) PLUS the current market value of your Gold and Stocks.
2. Subtract your immediate short-term debts.
3. **The Nisab Check:** Create a cell for the current value of 85 grams of gold.
4. **Zakat Due:** Write an `IF` statement. *IF Total Zakatable Wealth is greater than Nisab, then multiply Zakatable Wealth by 2.5% (0.025). Otherwise, 0.*

By building these five tabs step-by-step, you create a fully Shariah-compliant financial ecosystem. You log a transaction once in the Master Ledger, and the formulas will automatically update your 50/30/20 budget, your business profit, and your Zakat obligations simultaneously.
