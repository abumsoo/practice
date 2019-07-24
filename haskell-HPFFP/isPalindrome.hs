-- isPalindrome.hs
module IsPalindrome where

isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome x =
  first == (reverse last)
  where first = take (div (length x) 2) x
        last = drop (div (length x) 2 + (mod (length x) 2)) x
