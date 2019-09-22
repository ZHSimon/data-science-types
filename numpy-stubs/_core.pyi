"""
Numpy's mypy stub. Only type declarations for ndarray, the scalar hierarchy and array creation
methods are provided.
"""

from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    IO,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from pathlib import Path
import builtins

class dtype: ...

_dtype = dtype

_ShapeType = Union[int, Tuple[int, ...], List[int]]
_AxesType = Union[int, Tuple[int, ...], List[int]]
_OrderType = Union[str, Sequence[str]]
_DtypeType = Union[dtype, type]

# all the python types that an ndarray can have
_AnyNum = Union[int, float, bool]
# generic types that are only allowed to take on values from _AnyNum
_Num = TypeVar('_Num', int, float, bool)
_Num2 = TypeVar('_Num2', int, float, bool)

_T = TypeVar('_T')
NestedList = Union[List[_T], List[List[_T]], List[List[List[_T]]], List[List[List[List[_T]]]]]

class ndarray(Generic[_Num]):
    """
    "array-like" interface that both numpy.ndarray and all scalars (descendants of numpy.generic)
    implement this interface.
    """

    #
    # Array-like structures attributes
    #
    dtype: _dtype
    size: int
    ndim: int
    shape: Tuple[int, ...]

    #
    # Array-like methods
    #
    def __init__(
        self,
        shape: Tuple[int, ...],
        dtype: Optional[_DtypeType] = ...,
        buffer: Optional[Any] = ...,
        offset: Optional[int] = ...,
        strides: Optional[Tuple[int, ...]] = ...,
        order: Optional[str] = ...,
    ) -> None: ...
    def all(self, axis: Optional[_AxesType] = ..., keepdims: bool = ...) -> ndarray[_Num]: ...
    def any(self, axis: Optional[_AxesType] = ..., keepdims: bool = ...) -> ndarray[_Num]: ...
    def argmax(self, axis: Optional[int] = ...) -> ndarray[_Num]: ...
    def argmin(self, axis: Optional[int] = ...) -> ndarray[_Num]: ...
    # def argpartition(self, kth: Union[int, Sequence[int]], axis: Optional[int]=-1,
    #                  kind: str='introselect', order: _OrderType=None) -> ndarray[_Num]: ...
    def argsort(
        self, axis: Optional[int] = ..., kind: str = ..., order: Optional[_OrderType] = ...
    ) -> ndarray[_Num]: ...
    def astype(
        self, dtype: Any, order: str = ..., casting: str = ..., subok: bool = ..., copy: bool = ...
    ) -> ndarray[_Num]: ...
    def byteswap(self, inplace: bool = ...) -> ndarray[_Num]: ...
    def choose(self, choices: Sequence[ndarray[_Num]], mode: str = ...) -> ndarray[_Num]: ...
    def clip(self, a_min: Any, a_max: Any) -> ndarray[_Num]: ...
    def compress(self, condition: Sequence[bool], axis: Optional[int] = ...) -> ndarray[_Num]: ...
    def conj(self) -> ndarray[_Num]: ...
    def conjugate(self) -> ndarray[_Num]: ...
    def copy(self, order: str = ...) -> ndarray[_Num]: ...
    def cumprod(self, axis: Optional[int] = ..., dtype: Optional[Any] = ...) -> ndarray[_Num]: ...
    def cumsum(
        self, axis: Optional[int] = ..., dtype: Optional[_DtypeType] = ...
    ) -> ndarray[_Num]: ...
    def diagonal(self, offset: int = ..., axis1: int = ..., axis2: int = ...) -> ndarray[_Num]: ...
    def dot(self, b: ndarray[_Num]) -> ndarray[_Num]: ...
    def dump(self, file: str) -> None: ...
    def dumps(self) -> str: ...
    # def fill(self, value: _S) -> None: ...
    def flatten(self, order: str = ...) -> ndarray[_Num]: ...
    def getfield(self, dtype: _DtypeType, offset: int = ...) -> ndarray[_Num]: ...
    def item(self) -> _Num: ...
    def itemset(self, arg0: Union[int, Tuple[int, ...]], arg1: Optional[Any] = ...) -> None: ...
    def max(self) -> _Num: ...
    def mean(self) -> float: ...
    def min(self) -> _Num: ...
    def newbyteorder(self, new_order: str = ...) -> ndarray[_Num]: ...
    def nonzero(self) -> Tuple[ndarray[int], ...]: ...
    def partition(
        self, kth: _AxesType, axis: int = ..., kind: str = ..., order: Optional[_OrderType] = ...
    ) -> None: ...
    def prod(
        self,
        axis: Optional[_AxesType] = ...,
        dtype: Optional[_DtypeType] = ...,
        keepdims: bool = ...,
    ) -> ndarray[_Num]: ...
    def ptp(self, axis: Optional[int] = ...) -> ndarray[_Num]: ...
    def put(self, ind: ndarray[_Num], v: ndarray[_Num], mode: str = ...) -> None: ...
    def ravel(self, order: str = ...) -> ndarray[_Num]: ...
    def repeat(
        self, repeats: Union[int, Sequence[int]], axis: Optional[int] = ...
    ) -> ndarray[_Num]: ...
    def reshape(self, newshape: _ShapeType, order: str = ...) -> ndarray[_Num]: ...
    def resize(self, new_shape: _ShapeType, refcheck: bool = ...) -> None: ...
    def round(self, decimals: int = ...) -> ndarray[_Num]: ...
    # def searchsorted(self, v: Union[_S, ndarray[_Num]], side: str='left',
    #                  sorter: ndarray[_Num]=None) -> ndarray[_Num]: ...
    def setfield(self, val: Any, dtype: _DtypeType, offset: int = ...) -> None: ...
    def setflags(
        self, write: Optional[bool] = ..., align: Optional[bool] = ..., uic: Optional[bool] = ...
    ) -> None: ...
    def sort(self, axis: int = ..., kind: str = ..., order: Optional[_OrderType] = ...) -> None: ...
    def squeeze(self, axis: Optional[_AxesType] = ...) -> ndarray[_Num]: ...
    def std(
        self,
        axis: Optional[_AxesType] = ...,
        dtype: Optional[_DtypeType] = ...,
        ddof: int = ...,
        keepdims: bool = ...,
    ) -> ndarray[_Num]: ...
    def sum(self) -> _Num: ...
    def swapaxes(self, axis1: int, axis2: int) -> ndarray[_Num]: ...
    def take(
        self, indices: Sequence[int], axis: Optional[int] = ..., mode: str = ...
    ) -> ndarray[_Num]: ...
    def tobytes(self, order: str = ...) -> bytes: ...
    def tofile(
        self,
        fid: object,
        sep: str = ...,  # TODO fix fid definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
        format: str = ...,
    ) -> None: ...
    def tolist(self) -> List: ...
    def tostring(self, order: str = ...) -> bytes: ...
    def trace(
        self,
        offset: int = ...,
        axis1: int = ...,
        axis2: int = ...,
        dtype: Optional[_DtypeType] = ...,
    ) -> ndarray[_Num]: ...
    def transpose(self, axes: Optional[_AxesType] = ...) -> ndarray[_Num]: ...
    def var(
        self,
        axis: Optional[_AxesType] = ...,
        dtype: Optional[_DtypeType] = ...,
        ddof: int = ...,
        keepdims: bool = ...,
    ) -> ndarray[_Num]: ...
    def view(
        self,
        dtype: Optional[Union[_DtypeType, Type['ndarray[_Num]']]] = ...,
        type: Optional[type] = ...,
    ) -> ndarray[_Num]: ...
    #
    # Magic methods
    #
    def __abs__(self) -> ndarray[_Num]: ...
    def __add__(self, value: object) -> ndarray[_Num]: ...
    def __and__(self, value: object) -> ndarray[_Num]: ...
    def __array__(self, dtype: Optional[_DtypeType] = ...) -> ndarray[_Num]: ...
    def __array_prepare__(self, context: Optional[object] = ...) -> ndarray[_Num]: ...
    def __array_wrap__(self, context: Optional[object] = ...) -> ndarray[_Num]: ...
    def __bool__(self) -> bool: ...
    def __complex__(self) -> complex: ...
    def __contains__(self, key: object) -> bool: ...
    def __copy__(self) -> ndarray[_Num]: ...
    def __deepcopy__(self) -> ndarray[_Num]: ...
    def __delattr__(self, name: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __dir__(self) -> List[str]: ...
    def __divmod__(self, value: object) -> Tuple[ndarray[_Num], ndarray[_Num]]: ...
    def __eq__(self, value: object) -> ndarray[bool]: ...  # type: ignore
    def __float__(self) -> float: ...
    def __floordiv__(self, value: object) -> ndarray[_Num]: ...
    def __ge__(self, value: object) -> ndarray[bool]: ...
    def __getattribute__(self, name: str) -> Any: ...
    @overload
    def __getitem__(self, key: Union[int, Tuple[int, ...]]) -> _Num: ...
    @overload
    def __getitem__(
        self,
        key: Union[
            Union[ndarray[bool], slice],
            Tuple[int, Union[slice, ellipsis]],
            Tuple[Union[slice, ellipsis], int],
            Tuple[Union[ndarray[bool], slice, Ellipsis], ...],
        ],
    ) -> ndarray[_Num]: ...
    def __gt__(self, value: object) -> ndarray[bool]: ...
    def __iadd__(self, value: object) -> ndarray[_Num]: ...
    def __iand__(self, value: object) -> ndarray[bool]: ...
    def __ifloordiv__(self, value: object) -> None: ...
    def __ilshift__(self, value: object) -> None: ...
    def __imatmul__(self, value: ndarray[_Num]) -> None: ...
    def __imod__(self, value: object) -> None: ...
    def __imul__(self, value: object) -> None: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __invert__(self) -> ndarray[_Num]: ...
    def __ior__(self, value: object) -> None: ...
    def __ipow__(self, value: object) -> None: ...
    def __irshift__(self, value: object) -> None: ...
    def __isub__(self, value: object) -> None: ...
    def __iter__(self) -> Iterator[_Num]: ...
    def __itruediv__(sel, value: object) -> None: ...
    def __ixor__(self, value: object) -> None: ...
    def __le__(self, value: object) -> ndarray[_Num]: ...
    def __len__(self) -> int: ...
    def __lshift__(self, value: object) -> ndarray[_Num]: ...
    def __lt__(self, value: object) -> ndarray[_Num]: ...
    def __matmul__(self, value: ndarray[_Num]) -> ndarray[_Num]: ...
    def __mod__(self, value: object) -> ndarray[_Num]: ...
    def __mul__(self, value: object) -> ndarray[_Num]: ...
    def __ne__(self, value: object) -> ndarray[_Num]: ...  # type: ignore
    def __neg__(self) -> ndarray[_Num]: ...
    def __or__(self, value: object) -> ndarray[_Num]: ...
    def __pos__(self) -> ndarray[_Num]: ...
    def __pow__(self, value: object) -> ndarray[_Num]: ...
    def __radd__(self, value: object) -> ndarray[_Num]: ...
    def __rand__(self, value: object) -> ndarray[_Num]: ...
    def __rdivmod__(self, value: object) -> Tuple[ndarray[_Num], ndarray[_Num]]: ...
    def __rfloordiv__(self, value: object) -> ndarray[_Num]: ...
    def __rlshift__(self, value: object) -> ndarray[_Num]: ...
    def __rmatmul__(self, value: object) -> ndarray[_Num]: ...
    def __rmod__(self, value: object) -> ndarray[_Num]: ...
    def __rmul__(self, value: object) -> ndarray[_Num]: ...
    def __ror__(self, value: object) -> ndarray[_Num]: ...
    def __rpow__(self, value: object) -> ndarray[_Num]: ...
    def __rrshift__(self, value: object) -> ndarray[_Num]: ...
    def __rshift__(self, value: object) -> ndarray[_Num]: ...
    def __rsub__(self, value: object) -> ndarray[_Num]: ...
    def __rtruediv__(self, value: object) -> ndarray[_Num]: ...
    def __rxor__(self, value: object) -> ndarray[_Num]: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __str__(self) -> str: ...
    def __sub__(self, value: object) -> ndarray[_Num]: ...
    def __truediv__(sel, value: object) -> ndarray[_Num]: ...
    def __xor__(self, value: object) -> ndarray[_Num]: ...

# numpy has types that are more specific than int and float, but we treat them simply as aliases
# TODO: do this correctly (see commented out code below for hints)
float32 = float
float64 = float
int16 = int
int32 = int
int64 = int

##
## numpy's scalar hierarchy (http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#scalars)
##

# _Scalar = TypeVar('_Scalar')

# class generic(Generic[_Scalar]): ...
# class bool_(generic[bool]): ...
# class number(generic[_Scalar], Generic[_Scalar]): ...
# class integer(number[int]): ...
# class signedinteger(integer): ...
# class byte(signedinteger): ...
# class short(signedinteger): ...
# class intc(signedinteger): ...
# class int_(signedinteger): ...
# class longlong(signedinteger): ...
# class int8(signedinteger): ...
# class int16(signedinteger): ...
# class int32(signedinteger): ...
# class int64(signedinteger): ...
# class unsignedinteger(integer): ...
# class ubyte(unsignedinteger): ...
# class ushort(unsignedinteger): ...
# class uintc(unsignedinteger): ...
# class uint(unsignedinteger): ...
# class ulonglong(unsignedinteger): ...
# class uint8(signedinteger): ...
# class uint16(signedinteger): ...
# class uint32(signedinteger): ...
# class uint64(signedinteger): ...
# class inexact(number[float]): ...
# class floating(inexact): ...
# class half(floating): ...
# class single(floating): ...
# class float_(floating): ...
# class longfloat_(floating): ...
# class float16(floating): ...
# class float64(floating): ...
# class float128(floating): ...
# class complexfloating(inexact): ...
# class csingle(complexfloating): ...
# class complex_(complexfloating): ...
# class clongfloat(complexfloating): ...
# class complex64(complexfloating): ...
# class complex128(complexfloating): ...
# class complex256(complexfloating): ...
# class flexible(generic[_Scalar], Generic[_Scalar]): ...
# class character(flexible[str]): ...
# class str_(character): ...
# class unicode_(character): ...
# class void(flexible[None]): ...

#
# Array creation routines
#
def array(
    object: Union[NestedList[_Num], ndarray[_Num]], dtype: Optional[_DtypeType] = ...
) -> ndarray[_Num]: ...
def arange(range_: int) -> ndarray[_Num]: ...
def asarray(a: Any, dtype: Optional[_DtypeType] = ..., order: Optional[str] = ...) -> ndarray: ...
def ascontiguousarray(a: Any, dtype: Optional[_DtypeType] = ...) -> ndarray: ...
def copy(a: Any, order: Optional[str] = ...) -> ndarray: ...
def empty(shape: _ShapeType, dtype: _DtypeType = ..., order: str = ...) -> ndarray: ...
def empty_like(
    a: Any, dtype: Optional[Any] = ..., order: str = ..., subok: bool = ...
) -> ndarray: ...
def eye(N: int, M: Optional[int] = ..., k: int = ..., dtype: _DtypeType = ...) -> ndarray: ...
def full(
    shape: _ShapeType, fill_value: Any, dtype: Optional[_DtypeType] = ..., order: str = ...
) -> ndarray: ...
def full_like(
    a: Any, fill_value: Any, dtype: Optional[_DtypeType] = ..., order: str = ..., subok: bool = ...
) -> ndarray: ...

# def fromfunction(
#     function: Callable[..., _S], shape: _ShapeType, dtype: _DtypeType = float
# ) -> ndarray[_S]: ...
def fromiter(iterable: Iterator, dytpe: _DtypeType, count: int = ...) -> ndarray: ...
def fromstring(
    string: str, dtype: _DtypeType = ..., count: int = ..., sep: str = ...
) -> ndarray: ...
def identity(n: int, dtype: Optional[_DtypeType] = ...) -> ndarray: ...
def load(file: Union[Path, IO]) -> Dict[str, ndarray]: ...
def loadtxt(
    fname: Any,
    dtype: _DtypeType = ...,
    comments: Union[str, Sequence[str]] = ...,
    delimiter: Optional[str] = ...,
    converters: Optional[Dict[int, Callable[[Any], float]]] = ...,
    skiprows: int = ...,
    usecols: Optional[Sequence[int]] = ...,
    unpack: bool = ...,
    ndmin: int = ...,
) -> ndarray: ...
def ones(shape: _ShapeType, dtype: Optional[_DtypeType] = ..., order: str = ...) -> ndarray: ...
def ones_like(
    a: Any, dtype: Optional[_DtypeType] = ..., order: str = ..., subok: bool = ...
) -> ndarray: ...
def savetxt(fname: str, X: ndarray, header: Optional[str] = ...) -> None: ...
def savez(file: Path, *args: ndarray, **kwds: ndarray) -> None: ...
def zeros(shape: _ShapeType, dtype: _DtypeType = ..., order: str = ...) -> ndarray: ...
def zeros_like(
    a: Any, dtype: Optional[_DtypeType] = ..., order: str = ..., subok: bool = ...
) -> ndarray: ...

#
# Array transformation routines
#
def astype(a: ndarray[_Num], dtype: _Num2) -> ndarray[_Num2]: ...
def ceil(a: ndarray[_Num]) -> ndarray[_Num]: ...
def concatenate(
    an: Union[List[ndarray[_Num]], Tuple[ndarray[_Num], ...]], axis: _AxesType = ...
) -> (ndarray[_Num]): ...
def diag(a: ndarray[_Num]) -> ndarray[_Num]: ...
def exp(a: ndarray[_Num]) -> ndarray[_Num]: ...
def expand_dims(a: ndarray[_Num], axis: _AxesType) -> ndarray[_Num]: ...
def hstack(tup: Tuple[ndarray[_Num], ...]) -> ndarray[_Num]: ...
def log(a: ndarray[_Num]) -> ndarray[_Num]: ...
def logical_and(x1: ndarray[bool], x2: ndarray[bool]) -> ndarray[bool]: ...
def matmul(a: ndarray[_Num], b: ndarray[_Num]) -> ndarray[_Num]: ...
def max(
    a: ndarray[_Num], axis: Optional[_AxesType] = ..., keepdims: bool = ...
) -> ndarray[_Num]: ...
def mean(a: ndarray, axis: Optional[_AxesType] = ..., keepdims: bool = ...) -> ndarray[float]: ...
def min(
    a: ndarray[_Num], axis: Optional[_AxesType] = ..., keepdims: bool = ...
) -> ndarray[_Num]: ...
def nonzero(a: ndarray) -> Tuple[ndarray[int], ...]: ...
def power(x1: ndarray[_Num], x2: Union[_AnyNum, ndarray[_Num]]) -> ndarray[_Num]: ...
def ravel(a: ndarray[_Num]) -> ndarray[_Num]: ...
def reshape(a: ndarray[_Num], newshape: _ShapeType) -> ndarray[_Num]: ...
def split(a: ndarray[_Num], split_dims: List[int]) -> List[ndarray[_Num]]: ...
def sqrt(a: ndarray) -> ndarray[float]: ...
def std(a: ndarray, axis: Optional[_AxesType] = ..., keepdims: bool = ...) -> ndarray[float]: ...
def sum(
    a: ndarray[_Num], axis: Optional[_AxesType] = ..., keepdims: bool = ...
) -> ndarray[_Num]: ...
def take(a: ndarray[_Num], indices: ndarray[int], axis: _AxesType = ...) -> ndarray[_Num]: ...
def trace(a: ndarray[_Num]) -> _Num: ...
def trae(a: ndarray[_Num]) -> ndarray[_Num]: ...
def unique(a: ndarray[_Num]) -> ndarray[_Num]: ...
def where(condition: ndarray[bool], x: ndarray[_Num], y: ndarray[_Num]) -> ndarray[_Num]: ...

#
# weird classes
#
class matrix:
    def __init__(self, data: Union[List, str], dtype: _DtypeType = ..., copy: bool = ...): ...
    def reshape(self, shape: _ShapeType) -> matrix: ...

#
# Specific values
#
inf: float
nan: float