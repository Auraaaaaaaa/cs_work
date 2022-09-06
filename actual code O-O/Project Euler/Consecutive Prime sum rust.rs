targetnum = 999983
//
primes = vec![];
for i in 2..99984 {
    for j in 2..i {
        if i % j == 0 {
            break;
        }
        else if primes.iter().sum::<u32>() == targetnum {
            break;
        }
    }
    primes.push(i);
}
println!("{:?}", primes);
println!("{}", primes.iter().sum::<u32>());