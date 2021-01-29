###  The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
#### Hint: The basic equation of a circle is x^2 + y^2 = r^2.


**Approach** -: **Using Monte Carlo Method**
<br>
- Let, center of the circle is origin i.e, (0,0) and radius is 1 unit. So co-ordinates of the circle is (1,0),(-1,0),(0,1),(0,-1).
- Now mark a square whose sides touches the circle such that cirlce is inscribed in the square so side of the square will be 2 unit.

- Monte carlo method uses random generated numbers to predict the result

- Generate uniform random number from region, at X-axis (-1,1) and from Y-axis (-1,1)
- check if random generated numbers x and y lies inside the circle or not
- if x^2+y^2<=1 than points lies inside the circle, so inside_circle_points+=1, else total_points+=1
- area of cirlce = πr^2 = π(1)^2 = π
- area of square = (side)^2 = (2)^2 = 4
- so (area of cirlce / area of square) = π/4
- also, area of circle = no of points inside the circle
- area of square = total generated points
- Hence, π = 4 * (no of points inside circle / total generated points )
