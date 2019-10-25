from nxtools import NxConanFile
from conans import tools


class CppIterToolsConan(NxConanFile):
    name = "cppitertools"
    version = "1.0.0-nx"
    url = "https://github.com/hoxnox/conan-cppitertools"
    license = "https://github.com/ryanhaining/cppitertools/blob/master/LICENSE.md"
    settings = "os", "compiler", "build_type", "arch"
    options = {"noop":[True, False]}
    default_options = "noop=False"
    build_policy = "missing"
    description = "Range-based for loop add-ons inspired by the Python builtins and itertools library."

    def do_source(self):
        self.retrieve("12b64673078a523afa95e11ceb4f515fc917c5e85c6abeeb224cd69d9ab780c6",
                [
                    "vendor://google/cppitertools/cppitertools-{v}.tar.gz".format(v=self.version),
                    "https://github.com/hoxnox/cppitertools/archive/{v}.tar.gz".format(v=self.version)
                ], "cppitertools-{v}.tar.gz".format(v=self.version))

    def do_package(self):
        tools.untargz("cppitertools-{v}.tar.gz".format(v=self.version))
        include_dir = "cppitertools-{v}".format(v=self.version)
        self.copy(pattern="*.hpp",        dst="include/cppitertools", src=include_dir)
        self.copy(pattern="internal",     dst="include/cppitertools", src=include_dir)

