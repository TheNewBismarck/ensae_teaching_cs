"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest


try:
    import src
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.special.propagation_epidemic import simulation, pygame_simulation
from src.ensae_teaching_cs.helpers.video_helper import make_video


class TestEpidemicPropagation(unittest.TestCase):

    def test_simulation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = simulation(fLOG=fLOG, iter=10)
        fLOG(res)

    def test_image_video(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_image_video")
        import pygame
        pygame_simulation(pygame, fLOG=fLOG, iter=10, folder=temp)
        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "epidemic.avi")
        v = make_video(png, out, size=(300, 300), format="XVID")
        assert v is not None


if __name__ == "__main__":
    unittest.main()
