A1=[1 1;2 1]
b1=[400;600]
c1=[16000;10000]

[sol_opti, valeur_opti]=karmarkar(A1,b1,c1)

disp("Solution optimal :")
disp(sol_opti)
disp("Valeur optimale :")
disp(valeur_opti)

A2=[-1 -3 0;1 1 -1]
b2=[-4;10]
c2=[-1;1;-1]

[sol_opti2, valeur_opti2]=karmarkar(A2,b2,c2)

disp("Solution optimal :")
disp(sol_opti2)
disp("Valeur optimale :")
disp(valeur_opti2)
