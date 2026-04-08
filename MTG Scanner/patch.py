import textwrap

# LicenseClient (smali)

def LicenseClient(path):
    with open(path, "r") as file:
        lines = file.readlines()
        output = []
        skip = False

        for line in lines:
            if skip:
                if ".end method" in line:
                    output.append(line.lstrip())
                    skip = False
                continue

            if ".method private performLocalInstallerCheck(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            output.append(line)

    with open(path, "w") as file:
        file.writelines(output)

# Patches

LicenseClient("pt.tscg.mtgmanager/smali_classes2/com/pairip/licensecheck/LicenseClient.smali") # Play Store Check