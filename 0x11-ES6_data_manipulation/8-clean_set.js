export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const list = Array.from(set).filter(
    (firstHalf) => (firstHalf ? firstHalf.includes(startString) : ''),
  ).map((secondHalf) => secondHalf.slice(startString.length)).join('-');
  return (list);
}
