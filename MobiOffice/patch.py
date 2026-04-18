import textwrap

# LicenseLevel (smali_classes3)

def LicenseLevel(path):
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

            if ".method public static a(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1
                        .annotation build Landroidx/annotation/Nullable;
                        .end annotation

                        sget-object v0, Lcom/mobisystems/registration2/types/LicenseLevel;->premium:Lcom/mobisystems/registration2/types/LicenseLevel;
                        return-object v0
                    """), "\t"))
                skip = True
                continue

            output.append(line)

    with open(path, "w") as file:
        file.writelines(output)

# OsFeaturesCheckProxy (smali_classes3)

def OsFeaturesCheckProxy(path):
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

            if ".method public canUseAddOnFonts(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public canUseJapaneseFonts(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public disableScanToWordExcel(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public hasAdMobId(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public hasCamera(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public hasOneDriveForBusiness(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public hasPremiumFeature(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public isExpired(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public isPremium(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public isTrial(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public offerPremium(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public showOxfordDictForPremium(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public showQuickPdf(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public supportPrint(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x1
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public supportSpellCheck(" in line:
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

LicenseLevel("com.mobisystems.office/smali_classes3/com/mobisystems/registration2/types/LicenseLevel.smali") # Premium License Level
OsFeaturesCheckProxy("com.mobisystems.office/smali_classes3/com/mobisystems/registration2/OsFeaturesCheckProxy.smali") # Premium Check - Free Check