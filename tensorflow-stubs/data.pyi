from typing import Iterator, Tuple, Union, TypeVar

from ._core import Tensor

_NestedGeneric = TypeVar(
    "_NestedGeneric", Tensor, Tuple[Tensor, ...], Tuple[Union[Tensor, Tuple[Tensor, ...]], ...]
)

class Dataset(Generic[_NestedGeneric]):
    #
    # magic methods
    def __iter__(self) -> Iterator[_NestedGeneric]: ...
    def batch(self, batch_size: int, drop_remainder: bool = ...) -> Dataset[_NestedGeneric]: ...
    #
    # class methods
    @staticmethod
    def from_tensor_slices(tensors: _NestedGeneric) -> Dataset[_NestedGeneric]: ...
