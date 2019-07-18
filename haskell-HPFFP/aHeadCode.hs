-- Exercises: A Head Code
module AHeadCode where

multAdd = x * 3 + y
  where x = 3
        y = 1000

mult = x * 5
  where x = 10 * 5 + y
        y = 10

divAdd = z / x + y
  where x = 7
        y = negate x
        z = y * 10
