from main import StudentsInMLOps
import pytest

def test_enroll_students():
    obj = StudentsInMLOps()
    obj.enrollStudents(5)
    assert obj.getTotalStrength() == 5

def test_drop_students():
    obj = StudentsInMLOps()
    obj.enrollStudents(10)
    obj.dropStudents(3)
    assert obj.getTotalStrength() == 7

def test_get_class_name():
    obj = StudentsInMLOps()
    assert obj.getClassName() == "StudentsInMLOps"

if __name__ == '__main__':
    pytest.main()
