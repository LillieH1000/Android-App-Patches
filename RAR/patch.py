import textwrap

def AdsNotify(path):
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

            if ".method public static show(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 0

                        return-void
                    """), "\t"))
                skip = True
                continue

            output.append(line)

    with open(path, "w") as file:
        file.writelines(output)

AdsNotify("com.rarlab.rar/smali/com/rarlab/rar/AdsNotify.smali")