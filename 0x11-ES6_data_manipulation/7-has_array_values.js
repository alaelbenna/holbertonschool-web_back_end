export default function hasValuesFromArray(set, ArrayElement) {
  const bool = ArrayElement.every((boolean) => set.has(boolean));
  return (bool);
}
