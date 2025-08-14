from  agents import Agent, Runner, RunContextWrapper, function_tool
from connection import config
from pydantic import BaseModel
import rich
import asyncio

# Exercise : 01 BANK ACCOUNT CONTEXT


# Class for context
class BankAccount(BaseModel):
    account_number: int | str
    customer_name: str
    account_balance: float
    account_type: str

# Account holder profile 
bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Sabreena",
    account_balance=75500.50,
    account_type="Current"
)
@function_tool
def Bank_info(wrapper: RunContextWrapper[BankAccount]):
    account = wrapper.context
    return (
        f"Here is your bank acount info: \n"
        f"[cyan]Accout Number:[/cyan] {account.account_number}\n"
        f"[cyan]Customer Name:[/cyan] {account.customer_name}\n"
        f"[cyan]Account Balance:[/cyan] {account.account_balance}\n"
        f"[cyan]Account Type:[/cyan] {account.account_type}\n"
    )

Main_agent = Agent(
    name = "Info Agent",
    instructions= 
    """
    You are main agent. Your task is to provide bank account info by using bank info tool.
    Must use this tool for answering user query.
    """,
    tools= [Bank_info]
)

async def main():
    prompt_1= "Give me complete my bank account information."
    result = await Runner.run(
        Main_agent,
        prompt_1,
        run_config = config,
        context = bank_account
    )
    rich.print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())


