import textwrap

# AdsNotify (smali)

def AdsNotify(path):
    with open(path, "r") as file:
        lines = file.readlines()

        output = []
        method = False
        skip = False

        for line in lines:
            if ".method public static show(" in line:
                method = True
                output.append(line)
                continue

            if method:
                if ".locals" in line and "7" in line:
                    output.append(line)
                    output.append(textwrap.indent(textwrap.dedent("""
                        return-void
                    """), "\t"))
                    skip = True
                    continue

                if skip:
                    if ".end method" in line:
                        method = False
                        output.append(line.lstrip())
                        skip = False
                    continue

                output.append(line)
            else:
                output.append(line)

    with open(path, "w") as file:
        file.writelines(output)

# Patches

AdsNotify("com.rarlab.rar/smali/com/rarlab/rar/AdsNotify.smali")