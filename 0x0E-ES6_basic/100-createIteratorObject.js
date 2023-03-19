export default function createIteratorObject(report) {
  let allEmployees = [];
  for (const res of Object.values(report.allEmployees)) {
    allEmployees = [
      ...allEmployees,
      ...res,
    ];
  }

  return allEmployees;
}
