"""
    Creating a 3D sphere in a 2D space...
    
    Ray-Tracing Algorithm simplified: 
        -Shoot a ray towards each pixel
        -Find the nearest object hit by the ray in the scene
        -If hit, then find color at surface of the object
        
    Ray-Sphere intersection cases:
        -ray1 // interesects at 2 points
        -ray2  // intersects at 1 point
        -ray3 // does not intersect at all
        
            sphere_to_ray = ray>origin - sphere>center 
            
    Ray-Sphere intersection formula:
        a = 1
        b = 2 * ray>dir * sphere_to_ray
        c = sphere_to_ray * sphere_to_ray - (sphere>center)**2
        discriminant = b**2 - 4 * a * c 
        
        -discriminant > 0 // interesects at 2 points
        -discriminant = 0  // intersects at 1 point
        -discriminant < 0 // does not intersect at all
        
        Distance to point of intersection from ray>origin 
            dist = -b +- sqrt(discriminant) / 2 * a
        (we only need the closest intersection so replace +- with just -, ignoring negative distances )
        
    Hit position:
        Equation for a ray: 
             
            ray(t) = ray>origin + ray>direction * t
        
        Replace t with distance to get the hit position:
        
        hit>pos = ray>origin + ray>direction * dist
        
    Color at hit position:
        Using a plain color for now 
        
    Aspect ratio:
        Imagine the rendered image is a window to a 3D scene:
        
            x>min = -1 becomes left edge
            x>max = +1 becomes the right edge
            
        Image width wil typically be different from the height e.g. 320 x 200
        y cannot range from +1 and -1 - It has to be adjusted by the aspect ratio to prevent distortion 
        
        AspectRatio = width / height = 320 / 200 = 1.6
        
        y>max = 1 / AspectRatio = 1 / 1.6 = +0.625 // becomes bottom edge 
        y>min = -.625 becomes top edge
        
            TODO:
    Render a sphere into a 320 x 200 image
    
    Camera position: (0, 0, -1)
    Ball position & radius: (0, 0, 0) & 0.5
    Ball color: #FF0000 - RED 
    
"""

class Ray:
    """The ray is a half-line that instantiates an origin and a normalized direction """
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
        
        