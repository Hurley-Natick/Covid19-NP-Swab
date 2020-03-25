import math
import sys

fil_d = 1.75
nozzle_d = 0.4

header = """
; BJG custom
M104 S{ntemp} ; start nozzle heat
M140 S{btemp} ; start bed heat
M109 S{ntemp} ; wait for nozzle temp to 215
M190 S{btemp} ; wait for bed to hit temp
; BJG custom

G21 ;metric values
G90 ;absolute positioning
M83 ;set extruder in relative
M106 ;start with the fan on for filament cooling
G28 X0 Y0 ;move X/Y to min endstops
G28 Z0 ;move Z to min endstops
G29 ;run auto bed leveling
G1 Z15.0 F9000 ;move the platform down 15mm
G92 E0 ;zero the extruded length
G1 F200 E10 ;extrude 10mm of feed stock
G92 E0 ;zero the extruded length again
G1 F9000
"""

footer = """
M104 S0 ;extruder heater off
M140 S0 ;heated bed heater off (if you have it)
G91 ;relative positioning
G1 E-1 F300  ;retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F9000 ;move Z up a bit and retract filament even more
G28 X0 Y0 ;move X/Y to min endstops, so the head is out of the way
M84 ;steppers off
G90 ;absolute positioning"
"""

swab = """
; un-retract?
G0 X{sx:0.4f} Y{sy:0.4f} Z{sz:0.4f} F9000 ;go to start
G1 X{ex:0.4f} Y{ey:0.4f} Z{ez:0.4f} E{fl:0.4f} F{fr:0.4f} ;move and extrude
; retract?
"""

def make_path(pts, f, td):
    ppt = pts.pop(0)
    px, py, pz = ppt
    s = "G0 X{x:0.4f} Y{y:0.4f} Z{z:0.4f} F9000\n".format(x=px, y=py, z=pz)
    for pt in pts:
        x, y, z = pt
        px, py, pz = ppt
        l = math.sqrt(
            (x - px) ** 2 +
            (y - py) ** 2 +
            (z - pz) ** 2)
        tv = cyl_vol(td / 2., l)
        e = cyl_len(fil_d / 2., tv)
        s += "G0 X{x:0.4f} Y{y:0.4f} Z{z:0.4f} F{f:0.4f} E{e:0.4f}\n".format(
            x=x, y=y, z=z, e=e, f=f)
        ppt = pt
    return s


make_header = lambda ntemp, btemp: header.format(ntemp=ntemp, btemp=btemp)
make_footer = lambda: footer
cyl_vol = lambda r, l: math.pi * r ** 2 * l
cyl_len = lambda r, v: v / (math.pi * r ** 2.)
cyl_r = lambda l, v: math.sqrt(v / (math.pi * l))



def make_swab(sx, sy, sz, l, td, fr):
    assert td > nozzle_d * 0.1 and td < nozzle_d * 10
    tv = cyl_vol(td / 2., l)
    #fl = cyl_len(fil_d / 2., tv)
    fl = cyl_len(fil_d / 2., tv)
    print("Swab will extrude %s mm filament in %s seconds" % (fl, l / fr))
    # using track diameter, calculate filament length
    sx = sx
    sy = sy
    sz = sz
    fr = fr
    ex = sx
    ey = sy + l
    ez = sz
    return swab.format(sx=sx, sy=sy, sz=sz, ex=ex, ey=ey, ez=ez, fl=fl, fr=fr)


def draw_swab(z, sx=10, sy=10):
    xypts = [
        (0, 1),
        (0, 101),
        (-1, 101),
        (-1, 1),
        (0, 0),
        (0, -50),
        (1, -51),
        (1, -55),
        (0, -56),
        (-1, -56),
        (-2, -55),
        (-2, -51),
        (-1, -50),
        (-1, 0),
    ]
    xz = -min(p[0] for p in xypts)
    yz = -min(p[1] for p in xypts)
    pts = []
    for xy in xypts:
        x, y = xy
        pts.append((sx + xz + x, sy + yz + y, z))
    return pts


if __name__ == '__main__':
    fn = None
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    pfr = 600
    s = '\n'.join((
        make_header(210, 55),
        make_path(draw_swab(0.6, 10), pfr, 0.8),
        make_path(draw_swab(0.6, 20), pfr, 0.8),
        make_path(draw_swab(0.6, 30), pfr, 0.8),
        make_path(draw_swab(0.6, 40), pfr, 0.8),
        make_path(draw_swab(0.6, 50), pfr, 0.8),

        # retract, pause to add fabric, TODO not sure if this works
        "G0 X0 Y100 Z50 F9000 E-0.5; G4 S20; G0 E0.5\n",

        make_path(draw_swab(1.2, 10), pfr, 0.8),
        make_path(draw_swab(1.2, 20), pfr, 0.8),
        make_path(draw_swab(1.2, 30), pfr, 0.8),
        make_path(draw_swab(1.2, 40), pfr, 0.8),
        make_path(draw_swab(1.2, 50), pfr, 0.8),

        #make_swab(10, 10, 0.6, 30, 0.8, pfr),
        #make_swab(15, 10, 0.6, 30, 0.8, pfr),
        #make_swab(20, 10, 0.6, 30, 0.8, pfr),
        #make_swab(10, 10, 1.2, 30, 0.8, pfr),
        #make_swab(15, 10, 1.2, 30, 0.8, pfr),
        #make_swab(20, 10, 1.2, 30, 0.8, pfr),
        
        #make_swab(5, 10, 0.3, 30, 0.3, pfr),
        #make_swab(10, 10, 0.3, 30, 0.3, pfr),
        #make_swab(15, 10, 0.4, 30, 0.4, pfr),
        #make_swab(20, 10, 0.5, 30, 0.5, pfr),
        #make_swab(25, 10, 0.6, 30, 0.6, pfr),
        #make_swab(30, 10, 0.7, 30, 0.7, pfr),
        #make_swab(35, 10, 0.8, 30, 0.8, pfr),  # ok
        #make_swab(40, 10, 0.9, 30, 0.9, pfr),  # bad
        make_footer(),
    ))
    if fn is None:
        print(s)
    else:
        with open(fn, 'w') as f:
            f.write(s)
