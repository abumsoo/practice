-- strings.hs
module Strings where

getTail x = tail x

addToEnd x y = x ++ y

charAt x y = x !! y

skip x y = drop y x

thirdLetter :: String -> Char
thirdLetter x = x !! 2

letterIndex :: Int -> Char
letterIndex x = "Curry is awesome!" !! x

rvrs :: String
awesomeCurry = "Curry is awesome!"
rvrs = take 7 (drop 9 awesomeCurry) ++ take 4 (drop 5 awesomeCurry) ++ take 5 awesomeCurry
