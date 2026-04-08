import textwrap

# LicenseClient (smali)

def LicenseClient(path):
    with open(path, "r") as file:
        lines = file.readlines()

        output = []
        method = False
        skip = False

        for line in lines:
            if ".method private performLocalInstallerCheck(" in line:
                method = True
                output.append(line)
                continue

            if method:
                if ".locals" in line and "6" in line:
                    output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
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

    with open(path, "w") as file:
        file.writelines(output)

# Patches

LicenseClient("pt.tscg.mtgmanager/smali_classes2/com/pairip/licensecheck/LicenseClient.smali") # Play Store Check