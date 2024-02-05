from pathlib import Path
from typing import List, Optional
from PIL.ImageFont import load_default
from PIL.Image import Image, open as openImage, new as newImage
from PIL.ImageDraw import Draw


class ImagePathBuilder:

    def __init__(self) -> None:
        self.fontSize = 50
        self.textWidth = 100
        self.ftextHeight = 50

        self.images: List[Image] = []
        self.filenames: List[str] = []
        self.mergedImage: Optional[Image] = None

    def load(self, filepath: Path, filenames: List[str]) -> None:
        self.filenames = filenames
        for f in filenames:
            filename: str = f[:2]
            pathToImage = filepath.joinpath(filename + '.png')
            with openImage(pathToImage) as image:
                self.images.append(image.copy())

    def writeText(self) -> None:
        for index, filename in enumerate(self.filenames):
            nextIndex = index + 1
            if nextIndex < len(self.filenames):
                text = filename + f" -> {self.filenames[nextIndex][:2]}"
            else:
                text = filename
            image = self.images[index]
            self.__write(image, text)

    def merge(self, vertical: bool = True) -> None:
        if vertical:
            width = max(image.width for image in self.images)
            height = sum(image.height for image in self.images)
        else:
            width = sum(image.width for image in self.images)
            height = max(image.height for image in self.images)
        mergedImage = newImage("RGB", (width, height))
        currentX = 0
        currentY = 0
        for image in self.images:
            mergedImage.paste(image, (currentX, currentY))
            if vertical:
                currentY += image.height
            else:
                currentX += image.width
        self.mergedImage = mergedImage

    def show(self) -> None:
        if self.mergedImage:
            self.mergedImage.show()

    def __write(self, image: Image, text: str) -> None:
        draw = Draw(image)
        font = load_default(size=self.fontSize)
        position = (
            (image.width - self.textWidth) // 2,
            (image.height - self.textHeight) // 2,
        )
        draw.text(
            position, text, font=font, fill="white"
        )
