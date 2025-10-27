def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} → {destination}")
    towers_of_hanoi(n - 1, auxiliary, source, destination)

# Main Program
n = int(input("Enter the number of disks: "))
print("Steps to solve the Towers of Hanoi problem:")
towers_of_hanoi(n, 'A', 'B', 'C')