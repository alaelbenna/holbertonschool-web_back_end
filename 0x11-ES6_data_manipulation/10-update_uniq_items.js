export default function updateUniqueItems(items) {
  if (items instanceof Map) {
    for (const item of items) {
      if (item[1] === 1) items.set(item[0], 100);
    }
  } else throw new Error('Cannot process');
  return items;
}
