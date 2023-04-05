export const weakMap = new WeakMap();
export function queryAPI(point) {
  let apiCall = 0;
  if (weakMap.has(point)) {
    apiCall = weakMap.get(point);
  }
  weakMap.set(point, apiCall + 1);
  if (1 + apiCall >= 5) {
    throw (Error('Endpoint load is high'));
  }
}
