fn main() {
    let mut prime_to_find  = 10001;
    let mut list_primes = vec![];
    let mut x = 2;
    while(list_primes.len() < prime_to_find) { 
        if all(x % prime for prime in &list_primes) { 
            list_primes.push(x);
        }
        x +=1;
    }
    println!("{}",list_primes[-1]);
}