export default function getListStudentIds(students) {
  const mapping = Array.isArray(students);
  if (mapping) {
    const ids = students.map((items) => items.id);
    return (ids);
  }
  return [];
}
