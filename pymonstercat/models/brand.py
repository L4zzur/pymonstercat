from enum import IntEnum


class Brand(IntEnum):
    """Label's brand enum

    Attributes:
        uncaged (`int`): Uncaged Brand
        instinct (`int`): Instinct Brand
        silk (`int`): Silk Brand
        call_of_the_wild (`int`): Call of The Wild Podcast
        silk_showcase (`int`): Silk Showcase Podcast
    """

    uncaged = 1
    instinct = 2
    silk = 4
    call_of_the_wild = 3
    silk_showcase = 5
