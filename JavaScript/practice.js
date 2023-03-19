arr = [1, 2, 3, 4]
function combinations(arr, n){
  if (n==1) return arr.map((v) => [v]);
  const result = [];
  
  arr.forEach((fixed, idx, arr) => {
      const rest = arr.slice(idx + 1);
      const combis = combinations(rest, n-1);
      const combine = combis.map((v) => [fixed, ...v]);
      result.push(...combine)
  });
  return result
}

console.log(combinations(arr, 3))