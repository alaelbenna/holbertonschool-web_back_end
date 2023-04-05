export default function updateStudentGradeByCity(arrObj, city, newGrade) {
  let response = arrObj.filter((stud) => stud.location === city);

  response = response.map((students) => {
    const student = students;
    const score = newGrade.filter((x) => student.id === x.studentId);
    if (score.length > 0) {
      student.grade = score[0].grade;
    } else {
      student.grade = 'N/A';
    }
    return (student);
  });

  return (response);
}
