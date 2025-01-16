---

# **AI-Powered Financial and Web Search Agent**

This project leverages advanced AI capabilities to provide actionable financial insights and real-time web search capabilities. The agents are built using the Phi framework with the Groq LLM (Llama 3.3-70B Versatile) as the backbone. The system integrates web search and financial tools to deliver summarized, structured, and actionable recommendations.

---

## **Features**
- **Multi-Agent Collaboration**:
  - A **Web Search Agent** to gather real-time, high-quality financial data from reliable sources.
  - A **Financial Agent** to analyze stock performance, analyst recommendations, and company news.
- **Real-Time Stock Analysis**: Allows the user to input a stock ticker and receive a summary of its performance, along with actionable financial advice.
- **Comprehensive Outputs**:
  - Summarized insights in markdown format for clarity.
  - Structured tables for stock prices, analyst recommendations, and market news.
- **User-Centric Design**:
  - Simple command-line interface to input stock tickers.
  - High-quality data ensured via reliable tools like DuckDuckGo and YFinance.

---

## **Tech Stack**
- **Programming Language**: Python
- **AI Model**: Llama 3.3-70B Versatile (Groq)
- **Framework**: Phi
- **Tools**:
  - DuckDuckGo for web search.
  - YFinance for financial data.
  - Dotenv for secure environment variable management.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or higher
- An API key for the Groq LLM
- Access to the Phi framework and tools

### **Installation**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-financial-web-agent.git
   cd ai-financial-web-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add the following:
     ```
     GROQ_API_KEY=your_groq_api_key
     ```

4. **Run the project**:
   ```bash
   python main.py
   ```

---

## **Usage**
1. Run the program:
   ```bash
   python main.py
   ```
2. Enter the stock ticker symbol when prompted (e.g., `TSLA` for Tesla).
3. Receive a detailed analysis of the stock's performance, including:
   - Stock price trends
   - Analyst recommendations
   - Relevant news summaries
   - Actionable financial advice (e.g., "Buy", "Sell", "Hold").

---

## **Project Structure**
```
├── main.py               # Main script to run the project
├── agents/               # Contains agent configuration files
├── tools/                # Tools for financial and web data extraction
├── .env                  # Environment variables (not included in version control)
├── README.md             # Project documentation
├── requirements.txt      # List of dependencies
```

---

## **Sample Output**
### **Input**: `TSLA` (Tesla stock)
### **Output**:
```
Tesla Stock Performance (Past Week)

| Date       | Opening Price | Closing Price | Analyst Rating | Relevant News |
|------------|---------------|---------------|----------------|---------------|
| 01-12-2025 | $220.15       | $230.50       | Strong Buy     | [Link to News]|

**Actionable Advice**:
Based on current trends, it is recommended to HOLD Tesla stock.
```

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For questions or feedback, reach out at:
- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

--- 

Feel free to modify this template as needed!
