// ----------- BEGIN INPUT ------------

N = 1; // INPUT N=p+1 -- used for r

// nl = Round(64./N); // Coarse
nx = 16; // number of cells in x-direction
ny = 32; // number of cells in y-direction
nz = 4; // number of cells in z-direction
//nl = Round(96./N); // Baseline
//nl = Round(128./N); // Fine

// ----------- END INPUT --------------

lx=2.0*Pi;
ly=2.0;
lz=Pi;

dx_avg = lx/nx;
Printf("dx+ = %g",dx_avg*550);

Point(1) = {0, 0, 0, dx_avg};
line[] = Extrude {lx, 0, 0.} {
  Point{1}; Layers{Round(nx)};
};

Physical Line(1) = {line[1]};
surface[] = Extrude {0, 0, lz} {
  Line{line[1]}; Layers{nz}; Recombine;
};

Printf("ny = %g",ny);

r = 1.2^(N/2);
h0 = 0.5*(1-r)/(1-r^(ny/2));
h=0.;
For i In {0:(ny-2)/2}
  h += h0*r^i;
  y[i] = h;
  y[ny-i-2] = 1-h;
EndFor
y[ny/2-1] = 0.5;
y[ny-1] = 1.;

For i In {0:ny/2-1}
  Printf("y+[%g] = %g", i, 2*550*y[i]);
  layer[i] = 1;
EndFor
For i In {0:ny-1}
  layer[i] = 1;
EndFor

volume[] = Extrude {0.0,ly,0.0} {
  Surface{surface[1]}; Layers{ layer[], y[] }; Recombine;
};

Mesh 3; // generate 3D mesh automatically

