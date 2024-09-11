from collections import deque

class Solution:
    def containVirus(self, isInfected) -> int:
        def neighbors(r, c):
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < len(isInfected) and 0 <= nc < len(isInfected[0]):
                    yield nr, nc

        def bfs(r, c):
            queue, region, walls, threat = deque([(r, c)]), set([(r, c)]), 0, set()
            while queue:
                x, y = queue.popleft()
                for nx, ny in neighbors(x, y):
                    if (nx, ny) not in region:
                        if isInfected[nx][ny] == 1:
                            queue.append((nx, ny))
                            region.add((nx, ny))
                        elif isInfected[nx][ny] == 0:
                            walls += 1
                            threat.add((nx, ny))
            return region, walls, threat

        total_walls = 0
        while True:
            regions, walls_needed, threats = [], [], []
            visited = set()
            for r in range(len(isInfected)):
                for c in range(len(isInfected[0])):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        region, walls, threat = bfs(r, c)
                        regions.append(region)
                        walls_needed.append(walls)
                        threats.append(threat)
                        visited.update(region)
            
            if not threats: break
            idx = max(range(len(threats)), key=lambda i: len(threats[i]))
            total_walls += walls_needed[idx]

            for r, c in regions[idx]:
                isInfected[r][c] = -1

            for i, threat in enumerate(threats):
                if i != idx:
                    for r, c in threat:
                        isInfected[r][c] = 1

        return total_walls

