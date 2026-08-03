from abc import ABC, abstractmethod


class CodingPlatform(ABC):

    @abstractmethod
    def fetch(self):
        pass