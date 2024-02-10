# Amazing-OOM-RS

## Introduction

An extremely short executable rust implementation to f**k the memory up.

## Code

```rust
fn main(){loop{Box::leak(0.into());}}
```

## Reason

1. `0.into()` simply generates a unique pointer with a clean ownership
2. `Box::leak()` simply forgets the input unique pointer's ownership, turning it into a raw pointer
3. Each time you leak a unique pointer, you don't give a try to free/drop it's load on heap memory
4. `loop{}` means this program will continue to be executed until all of the memory have been f**ked up

