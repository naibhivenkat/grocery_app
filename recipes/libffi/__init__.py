from pythonforandroid.recipe import AutoconfRecipe

class LibFFIFixRecipe(AutoconfRecipe):
    version = '3.3'
    url = 'https://github.com/libffi/libffi/releases/download/v{version}/libffi-{version}.tar.gz'

    def build_arch(self, arch):
        # Skip autogen.sh entirely
        self.apply_patches(arch)
        super().build_arch(arch)

recipe = LibFFIFixRecipe()
