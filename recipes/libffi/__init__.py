def build_arch(self, arch):
    import sh
    from pythonforandroid.logger import shprint
    build_dir = self.get_build_dir(arch.arch)
    env = self.get_recipe_env(arch)

    # Comment this out to skip autogen.sh
    # shprint(sh.Command('./autogen.sh'), _env=env)

    configure = sh.Command('./configure')
    shprint(configure, '--host=' + arch.command_prefix,
            '--disable-debug', '--disable-dependency-tracking',
            '--prefix=' + self.get_install_dir(arch), _env=env)
    shprint(sh.make, '-j5', _env=env)
    shprint(sh.make.install, _env=env)
