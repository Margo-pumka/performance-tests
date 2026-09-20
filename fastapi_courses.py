from fastapi import FastAPI, APIRouter, status, Path, Query, HTTPException
from pydantic import BaseModel, RootModel

app = FastAPI()

courses_router = APIRouter(
    prefix="/api/v1/courses",
    tags=["courses-service"])

class CourseIn(BaseModel):
    title: str
    max_score: int
    min_score: int
    description: str

class CourseOut(CourseIn):
    id: int

class CoursesStore(RootModel):
    root: list[CourseOut] = []

    def find(self, course_id: int) -> CourseOut | None:
        return next(filter(lambda course: course.id == course_id, self.root), None)

    def create(self, course: CourseIn) -> CourseOut:
        max_course_id = max((course.id for course in self.root), default=0)
        course = CourseOut(id=max_course_id + 1, **course.model_dump())
        self.root.append(course)
        return course


    def update(self, course: CourseIn, course_id: int) -> CourseOut:
        index = next(index for index, course in enumerate(self.root) if course.id == course_id)
        updated = CourseOut(id=course_id, **course.model_dump())
        self.root[index] = updated
        return updated

    def delete(self, course_id: int) -> None:
        self.root = [course for course in self.root if course.id != course_id]

store = CoursesStore()

@courses_router.post("",  response_model=CourseOut, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseIn):
    return store.create(course=course)

@courses_router.get("", response_model=list[CourseOut], status_code=status.HTTP_200_OK)
def get_courses():
    return store.root

@courses_router.get("/{course_id}", response_model=CourseOut, status_code=status.HTTP_200_OK)
def get_course(course_id: int = Path(ge=1)):
    if not (course := store.find(course_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found")
    return course

@courses_router.put("/{course_id}", response_model=CourseOut, status_code=status.HTTP_200_OK)
def update_course(course: CourseIn, course_id: int = Path(ge=1)):
    if not store.find(course_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found")
    return store.update(course=course, course_id=course_id)

@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int = Path(ge=1)):
    if not store.find(course_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found")
    store.delete(course_id)

app.include_router(courses_router)