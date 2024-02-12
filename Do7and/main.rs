fn main() {
    loop {
        let l = vec!['l'];
        std::mem::forget(l);
    }
    
}
