#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    srand(time(0)); // Seed for randomness
    int result = rand() % 2; // Random 0 or 1
    if (result == 0)
        std::cout << "Heads" << std::endl;
    else
        std::cout << "Tails" << std::endl;
    return 0;
}
