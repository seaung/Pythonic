#### os module and os.path module


>

    1. 常用os.path方法

        - os.path.abspath(path) return a normalized version of the pathname path

        - os.path.basename(path) return the base name of pathname path

            example:
                    where basename for '/food/bar' return bar

                    the basename() function return a empty string

        - os.path.dirname() return direct name path

        - os.path.exists(path) return True if path refers to an existing path an open file descriptor, return false for broking symbolic links

        - os.path.getatime() return the time of last time access of path

        - os.path.getsize() return the size in bytes of path

        - os.path.isabs(path) return True if path is an absolute pathname

        - os.path.isfile() return True if path an existing regularfile

        - os.path.isdir() return True if path is an existing directory
