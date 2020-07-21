def solution(x,y):
        newx = x + y - 1

        #calculating prisoner ID at (newx , 1)
        id_at_newx_y1 = int((newx * (newx+1))/ 2)

        id_at_x_y = id_at_newx_y1 - (y-1);
        string_sol = str(id_at_x_y)
        return string_sol

print(solution(5,10))



