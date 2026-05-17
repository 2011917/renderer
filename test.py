verticies = []

triangles = []

with open('square.obj', 'r') as file:
    for line in file.readlines():
        if line[0] == 'v':
            # 1. Clean off the trailing newline character (\n)
            cleaned_line = line.strip()

            # 2. Split by any amount of consecutive whitespace
            parts = cleaned_line.split()

            # 3. Double-check that it's a vertex line and unpack the coordinates
            if parts and parts[0] == 'v':
                x, y, z = parts[1], parts[2], parts[3]
                verticies.append([float(x), float(y), float(z)])

        if line[0] == 'f':
            # 1. Clean off the trailing newline character (\n)
            cleaned_line = line.strip()

            # 2. Split by any amount of consecutive whitespace
            parts = cleaned_line.split()

            # 3. Double-check that it's a vertex line and unpack the coordinates
            if parts and parts[0] == 'f':
                a, b, c = parts[1], parts[2], parts[3]
                triangles.append([int(a), int(b), int(c)])


print(verticies)
print(triangles)