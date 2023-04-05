export default function getStudentsByLocation(students, city) {
  const filter = Object.getPrototypeOf(students);
  if (filter === Array.prototype) {
    const specificCity = students.filter((items) => items.location === city);
    return (specificCity);
  }
  return [];
}
