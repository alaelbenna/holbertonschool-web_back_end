export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw (Error('Position outside range'));
  }
  const arrayBuffer = new ArrayBuffer(length);
  const data = new DataView(arrayBuffer, 0, length);
  data.setInt8(position, value);
  return (data);
}
