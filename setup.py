#!/usr/bin/env python
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from setuptools import setup, Command

from distutils.command.build_py import build_py

with open('README.rst') as infile:
    long_description = infile.read()

from libname import __version__

setup(name='libname',
      version=__version__,
      description='description',
      long_description=long_description,
      url='https://github.com/swifty94/$name',
      license='Simplified BSD License',
      author='Kirill Rudenko',
      author_email='some@email.com',
      packages=['libname'],
      provides=['libname'],
      scripts=['scripts/run'],
      install_requires=[''],
      cmdclass={'build_py': build_py},
      classifiers=[
                   "Programming Language :: Python",
                   "License :: OSI Approved :: BSD License",
                  ],
     )
