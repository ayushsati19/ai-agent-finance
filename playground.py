from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import getpass
from phi.playground import Playground, serve_playground_app
import phi.api
# Load environment variables
# Load environment variables from .env file
load_dotenv('.env',override=True)

phi.api=os.getenv('API_KEY')

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



app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=='__main__':
    serve_playground_app('playground:app',reload=True)