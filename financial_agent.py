from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import getpass

load_dotenv('.env',override=True)
if 'GROQ_API_KEY' not in os.environ:
    os.environ['GROQ_API_KEY']=getpass.getpass('GROQ_API_KEY')


web_search_agent=Agent(
    name='web_search_agent',
    role='search the web for the reliable financial data which can be used to get useful insight',
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    instructions=[
        'Focus on high-quality, trusted financial news sources (e.g., Bloomberg, Reuters, Yahoo Finance, etc.).',
        'Ensure all information is up-to-date, relevant, and fact-checked.',
        'Summarize findings in a structured format, with key insights in bullet points.',
        'Prioritize sources that provide detailed financial data (stock prices, analyst ratings, market trends, etc.).',
        'Always include source links and the date of publication.'
    ],
    show_tool_calls=True,
    markdown=True,
)
## Financial agent
finance_agent=Agent(
    name='finance_ai_agent',
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True),
       ],
    instructions=[
        'Present financial data in a structured table format (e.g., stock prices, analyst ratings, news summaries).',
        'Focus on high-quality, accurate financial data (e.g., stock performance, analyst recommendations, earnings reports).',
        'Provide a summary of key financial trends or insights based on the data.',
        'Offer actionable recommendations based on financial data (e.g., "Buy", "Sell", "Hold").',
        'Ensure all data is up-to-date, referencing the most recent financial reports and news articles.',
        'Cross-check the sources of data for consistency and accuracy.',
    ],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id='llama-3.3-70b-versatile'),
    instructions=[
        'Ensure seamless collaboration between the web search agent and finance agent to provide a comprehensive response.',
        'Search for the latest financial data, news, and analyst recommendations, and organize them in clear, structured tables.',
        'Summarize the findings in a concise manner, highlighting key insights and actionable recommendations.',
        'When providing stock data, ensure that you include stock price, analyst recommendations, and relevant market news.',
        'Use tables to present financial data clearly, and always include source links and the date of publication.',
        'When possible, cross-reference data from both agents to ensure consistency and reliability.',
        'Provide actionable financial advice based on the combined data (e.g., Buy, Sell, Hold).',
        'Display the results in markdown format for readability and clarity.',
    ],
    show_tools_calls=True,
    markdown=True,
)

# Ask the user for the stock they want to analyze
stock_name = input("Enter the stock ticker symbol you want to analyze (e.g., TSLA for Tesla): ")

# Use the inputted stock name in the agent's response
multi_ai_agent.print_response(
    f"Summarize {stock_name}'s stock performance for the past week, including the latest analyst recommendations and relevant news. Provide a table with the stock price, analyst recommendations, and company news. Conclude with actionable financial advice based on the current trends, including whether to buy, sell, or hold {stock_name} stock.",
    stream=True
)
