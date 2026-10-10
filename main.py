from fastmcp import FastMCP
import asyncio

from database import initialize_database
from crud import (
    add_expense,
    get_all_expenses,
    get_expenses_by_category,
    delete_expense,
    update_expense,
    get_total_expense,
    get_category_summary,
)

initialize_database()

mcp = FastMCP("Expense Tracker")


@mcp.tool
async def add_new_expense(
    amount: float,
    category: str,
    description: str,
    expense_date: str,
    payment_method: str,
):
    return await asyncio.to_thread(
        add_expense,
        amount,
        category,
        description,
        expense_date,
        payment_method,
    )


@mcp.tool
async def view_all_expenses():
    return await asyncio.to_thread(get_all_expenses)


@mcp.tool
async def view_expenses_by_category(category: str):
    return await asyncio.to_thread(get_expenses_by_category, category)


@mcp.tool
async def remove_expense(expense_id: int):
    return await asyncio.to_thread(delete_expense, expense_id)


@mcp.tool
async def edit_expense(
    expense_id: int,
    amount: float,
    category: str,
    description: str,
    expense_date: str,
    payment_method: str,
):
    return await asyncio.to_thread(
        update_expense,
        expense_id,
        amount,
        category,
        description,
        expense_date,
        payment_method,
    )


@mcp.tool
async def total_expense():
    return await asyncio.to_thread(get_total_expense)


@mcp.tool
async def category_summary():
    return await asyncio.to_thread(get_category_summary)


if __name__ == "__main__":
    mcp.run()