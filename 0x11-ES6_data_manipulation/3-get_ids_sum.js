import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(getListStudents) {
  const sum = (max, min) => max + min;
  const reduced = getListStudentIds(getListStudents).reduce(sum);
  return (reduced);
}
