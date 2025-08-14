from agents import Agent, Runner, RunContextWrapper, function_tool
from connection import config
from pydantic import BaseModel
import asyncio
import rich

# Exercise: 02 STUDENT PROFILE CONTEXT

# Class for context
class StudentProfile(BaseModel):
    student_id: str | int
    student_name: str
    current_semester: int
    total_courses: int

# Student profile 
student = StudentProfile(
    student_id = "STU-456",
    student_name = "Daniyal Pervaiz",
    current_semester = 4,
    total_courses = 5
)
@function_tool
def student_info(wrapper: RunContextWrapper[StudentProfile]):
    student = wrapper.context
    return(
        f"Here are the Student Profile Information: \n"
        f"[green]Student ID:[/green] {student.student_id}\n"
        f"[green]Student Name:[/green] {student.student_name}\n"
        f"[green]Current Semester:[/green] {student.current_semester}\n"
        f"[green]Total Courses:[/green] {student.total_courses}\n"
    )
# Main Agent
Student_agent = Agent(
    name = "Info Provider",
    instructions = 
    """
    You are an Academic Records Assistant. Your task is to retrieve and present student profile details 
    in a clear, organized format using the 'student_info' tool. Always ensure the response 
    is professional and easy to read.
    """,
    tools = [student_info]
)
async def main():
    prompt1 = "Show me all the academic information for the student."
    result = await Runner.run(
        Student_agent,
        prompt1,
        run_config = config,
        context = student
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
