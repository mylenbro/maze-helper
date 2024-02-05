from pathlib import Path
from PathFinder import PathFinder
from ImagePathBuilder import ImagePathBuilder


def main() -> None:
    map = 'dream'  # 'forest' 'dream'
    filepath = Path().resolve().joinpath(map)

    finder = PathFinder()
    finder.loadMap(filepath)
    path = finder.find(
        start="A2",
        end="D3",
        requiredNodes=["B3"],
        maxOccurrences=1
    )

    if not path:
        return print("No path found . . .")

    print(len(path))
    print(path)

    # builder = ImagePathBuilder()
    # builder.load(filepath, path)
    # builder.writeText()
    # builder.merge(vertical=True)
    # builder.show()


if __name__ == "__main__":
    main()
