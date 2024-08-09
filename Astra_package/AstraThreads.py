"""
This file contains updated thread class for Software.
"""

from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from typing import Any

class AstraThread(Thread):
    """
    Astra thread class inherited from 'Thread' class, has extra 'stop' method to stop thread. 
    """
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
     
    def terminate(self):
        """
        Method used to stop thread usding object of the class.
        """
        self._stop.set()