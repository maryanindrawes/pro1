from inheretance.ball import Ball
from inheretance.cylinder import Cylinder

b_1 = Ball(1)
print("The volume is = ", b_1.volume())
b_1.print_area()

cy = Cylinder(4, 20)
print("The area is = ", cy.area())
print("The mo7yt is = ", cy.Cir())
print("The area of the base :", cy.get_base())
