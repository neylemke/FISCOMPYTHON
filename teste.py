def f(n):
      curr = n
      tmp = 0
      while curr != 1:
        tmp = tmp + 1
        if curr % 2 == 1:
          curr = 3 * curr + 1
        else:
          curr = curr/2
      return tmp

%%hylang
(import math)
(defn safesqrt [x]
    (if (< x 0)
      (math.sqrt (- 0 x))
      (math.sqrt x)
    )
)
