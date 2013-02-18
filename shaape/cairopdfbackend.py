from cairobackend import CairoBackend
import cairo
import math
import os
import errno

class CairoPdfBackend(CairoBackend):
    def __init__(self):
        super(CairoPdfBackend, self).__init__()
        return

    def blur_surface(self):
        pass

    def new_surface(self, name = None):
        return cairo.PDFSurface(name, int(math.ceil(self.image_size()[0] + self.margin()[0] + self.margin()[1])), int(math.ceil(self.image_size()[1] + self.margin()[2] + self.margin()[3])))

    def export_to_file(self, filename):
        path = os.path.dirname(filename)
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        surface = self.new_surface(filename)
        ctx = cairo.Context(surface)
        ctx.set_source_surface(self.surfaces()[-1])
        ctx.paint()
        surface.finish()
        return
