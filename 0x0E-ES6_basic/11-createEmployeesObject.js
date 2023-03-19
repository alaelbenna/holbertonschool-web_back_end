export default function createEmployeesObject(departmentName, employees) {
  const value = [];
  for (const idx of employees) {
    value.push(idx);
  }
  const obj = {
    [`${departmentName}`]: value,
  };

  return obj;
}
