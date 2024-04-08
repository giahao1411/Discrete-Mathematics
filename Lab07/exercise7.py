def towerOfHanoi(n, source, destination, auxiliary):
    if n > 0:
        towerOfHanoi(n - 1, source, auxiliary, destination)

        disk = source[1].pop()
        destination[1].append(disk)

        print(f"Move disk {disk} from {source[0]} to {destination[0]}")

        towerOfHanoi(n - 1, auxiliary, destination, source)


source = ("A", [3, 2, 1])
destination = ("B", [])
auxiliary = ("C", [])
towerOfHanoi(3, source, destination, auxiliary)
