def parse_txt_maze(filename):
    rows = []

    with open(filename) as maze:
        contents = maze.read()
        lines = contents.splitlines()
        rows = list(map(lambda x: list(x), lines))
    
    height = len(rows)
    width =  max(len(row) for row in rows)
    
    for row in rows:
        print(row)
    
    return {
        "rows": rows,
        "height": height,
        "width": width
    }

