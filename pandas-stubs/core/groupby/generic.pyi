from typing import overload, List

from pandas.core.frame import DataFrame
from pandas.core.series import Series


class GroupBy: ...
class DataFrameGroupBy(GroupBy):
    @overload
    def __getitem__(self, item: str) -> Series: ...
    @overload
    def __getitem__(self, item: List[str]) -> DataFrame: ...
class SeriesGroupBy(GroupBy):
    def __getitem__(self, item: str) -> Series: ...