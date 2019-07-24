-- myAbs.hs
module MyAbs where

myAbs :: Int -> Int
myAbs x =
  if x < 0
  then negate x
  else x
