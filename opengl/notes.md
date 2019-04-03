# Shaders
Shaders are small programs which take care of each small process in the graphics
pipeline.
## Graphics pipeline
The graphics pipeline is what takes 3D coordinates and transforms them into 2D
pixels. 3D coordinates -> 2D coordinates -> colored 2D pixels.

Vertex data -> Vertex shader -> shape assembly -> geometry shader -> tests and
blending -> fragment shader -> rasterization

In order for OpenGL to know what to do with your collection of points, you must
give it a hint as to what render type you want to form with the data. That hint
is called a primitive. Some of these primitives are GL_POINTS, GL_TRIANGLES, and
GL_LINE_STRIP.

Steps of the pipeline:

- Vertex shader: takes input of single vertex. Transforms 3D coordinates into
  different 3D coordinates and allows us to do some basic processing on the
  vertex attributes
- Primitive assembly: takes as input all vertices from the vertex shader that
  form primitives and assembles all the points
- Geometry shader: takes as input a collection of vertices and has the ability
  to generate other shapes by emitting new vertices to form new or other
  primitives.
- Rasterization stage: maps the resulting primitives to the corresponding pixels
  on the final screen, resulting in fragments for the fragment shader to
  use. Before that, clipping is performed. Discards all fragments that are
  outside the view.
- Fragment shader: calculate the final color of a pixel
- Alpha test and blending: Checks corresponding depth value of the fragment and
  uses those to check if the resulting fragment is in front or behind other
  objects and should be discarded accordingly.

Normalized device coordinates - small space where x, y, and z lie between -1.0
and 1.0.
