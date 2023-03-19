// 소수구하기

// 1. O(n)
function is_prime(n) {
  for (let i = 2; i<n; i+= 1) {
    if (num%i == 0){
      return false;
    }
  }
  return true
} 

//2. O(sqrt(n))
function is_prime(n) {
  for (let i = 2; i*i<n; i+= 1) {
    if (num%i == 0){
      return false;
    }
  }
  return true
} 

//3. 에라토스테네스의 체 -> O(n log log n) 
function get_primes(n) {
  const prime = [false, false, ...Array(n-1).fill(true)];

  for (let i = 2; i*i<n; i+= 1) {
    if (prime[i]){
      for (let j= i*2; j<=n; j+=1) {
        prime[j] = false;
      }
    }
  }
  return prime.filter(Boolean);
} 