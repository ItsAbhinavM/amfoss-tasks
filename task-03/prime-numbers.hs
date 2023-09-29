import Control.Monad (forM_)

main :: IO ()
main = do
    putStrLn "Enter the number here : "
    n <- readLn
    forM_ [2..n-1] $ \i -> do
        if isPrime i
            then print i
            else pure ()

isPrime :: Int -> Bool
isPrime i = all (\b -> i `mod` b /= 0) [2..i-1]
