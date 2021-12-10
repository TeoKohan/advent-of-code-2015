import System.IO
import Data.List (group)

main = do  
    file <- readFile "input"
    let ls = lines file !! 0
    print(ls)
    let ns = map (read . pure :: Char -> Int) ls
    let a = length $ elvesGame 40 ns
    let b = length $ elvesGame 50 ns
    writeFile "output" (unlines[show a, show b])

elvesGame :: Int -> [Int] -> [Int]
elvesGame 0 xs  = xs
elvesGame n xs  = elvesGame (n-1) (concat . elves . group $ xs)

elves :: [[Int]] -> [[Int]]
elves []     = []
elves (x:xs) = [length x, x !! 0] : elves xs