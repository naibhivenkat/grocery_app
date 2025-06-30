from pythonforandroid.recipe import AutoconfRecipe
import sh
from os.path import join

class LibffiRecipe(AutoconfRecipe):
    version = '3.3'
    url = 'https://github.com/libffi/libffi/releases/download/v3.3/libffi-{version}.tar.gz'
    built_libraries = {'libffi.a': 'inst/lib'}
    def build_arch(self, arch):
        # Patch configure.ac before running autogen.sh
        configure_ac = join(self.get_build_dir(arch.arch), 'configure.ac')
        self.apply_patches(arch, [
            (configure_ac, 'LT_SYS_SYMBOL_USCORE',
             'm4_pattern_allow([LT_SYS_SYMBOL_USCORE])\nLT_SYS_SYMBOL_USCORE')
        ])
        super().build_arch(arch)

    def apply_patches(self, arch, patches):
        for file_path, find_str, replace_str in patches:
            if not self.ctx:
                continue
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                if find_str in content:
                    content = content.replace(find_str, replace_str)
                    with open(file_path, 'w') as f:
                        f.write(content)
            except FileNotFoundError:
                pass

recipe = LibffiRecipe()
