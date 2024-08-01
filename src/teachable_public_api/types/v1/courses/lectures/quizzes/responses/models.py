"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class QuizStudentResponses(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    percent_correct: int = pydantic.Field(alias="percent_correct")
    student_email: str = pydantic.Field(alias="student_email")
    student_id: int = pydantic.Field(alias="student_id")
    student_name: str = pydantic.Field(alias="student_name")
    submitted_at: str = pydantic.Field(alias="submitted_at")


class QuizResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    course_id: int = pydantic.Field(alias="course_id")
    course_name: str = pydantic.Field(alias="course_name")
    graded: bool = pydantic.Field(alias="graded")
    lecture_id: int = pydantic.Field(alias="lecture_id")
    lecture_name: str = pydantic.Field(alias="lecture_name")
    responses: typing.List[QuizStudentResponses] = pydantic.Field(alias="responses")