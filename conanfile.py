from conans import ConanFile
from conans import tools

class GnuplotiostreamConan(ConanFile):
    name = "gnuplot-iostream"
    version = "1.1"
    description = "C++ interface to gnuplot"
    url = "www.github.com/kwint/conan-gnuplot-iostream"
    repo_url = "https://github.com/dstahlke/gnuplot-iostream"
    license = "None"

    def source(self):
        self.run("git clone https://github.com/dstahlke/gnuplot-iostream.git")

    def package(self):
        self.copy("*.h", dst="include")
