"""
Generate CSS sprites given rectangle coordinates

Input file should look like:

190,144,560,239
190,239,687,341
191,622,688,677
190,358,348,392
502,358,680,392
191,393,398,418
193,420,456,455
193,453,456,497
193,496,456,537
494,395,627,471
495,471,628,547
495,548,628,624
175,831,688,912


Output will look like:

.image-1 {
    width: 370px;
    height: 95px;
    background-position: -190px -144px;
}
.image-2 {
    width: 497px;
    height: 102px;
    background-position: -190px -239px;
}
.image-3 {
    width: 497px;
    height: 55px;
    background-position: -191px -622px;
}
.image-4 {
    width: 158px;
    height: 34px;
    background-position: -190px -358px;
}
.image-5 {
    width: 178px;
    height: 34px;
    background-position: -502px -358px;
}
.image-6 {
    ...
    ...

"""

import sys

class CSS:

    def __init__(self):
        pass

    def make_sprite(self, coordinates):
        """ coordinates is a comma-separated string of ints """

        coords = [int(x) for x in coordinates.split(',')]

        assert len(coords) == 4, "Coordinates are not rectangular"

        start_x, start_y, upper_right, bottom_right = coords

        width  = upper_right - start_x
        height = bottom_right - start_y

        css = {}

        css['width']   = str(width)  + "px;"
        css['height']  = str(height) + "px;"

        css['background-position'] = "-" + str(start_x) + "px -" + str(start_y) + "px;"

        return css

    def make_sprites_from_file(self, filename):
        with open(filename) as f:
            data = f.read()

        coords = data.split('\n')[:-1]
        css_data = []
        for c in coords:
            css_data.append(self.make_sprite(c))

        for i, data in enumerate(css_data):
            print '.image-{0}'.format(i+1), "{"
            print '\t', 'width:',  data['width']
            print '\t', 'height:', data['height']
            print '\t', 'background-position:', data['background-position']
            print '}'


def main():
    css = CSS()
    filename = sys.argv[1]

    css.make_sprites_from_file(filename)

if __name__ == '__main__': sys.exit(main())
