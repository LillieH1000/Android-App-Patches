import textwrap

def Claim(path):
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

            if ".method public isShowAds(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public setShowAds(" in line:
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

def ManagerPreferencesHelper(path):
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

            if ".method public getShowAds(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public setShowAds(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 0

                        return-void
                    """), "\t"))
                skip = True
                continue

            if ".method public getFullAdsCounter(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public setFullAdsCounter(" in line:
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

def SubscriptionHelper(path):
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

            if ".method public final checkPremiumStatus(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 0

                        return-void
                    """), "\t"))
                skip = True
                continue

            if ".method public final redeemCode(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 0

                        return-void
                    """), "\t"))
                skip = True
                continue

            if ".method public final showPremium(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 0

                        return-void
                    """), "\t"))
                skip = True
                continue

            if ".method public final showPremiumScreen(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 0

                        return-void
                    """), "\t"))
                skip = True
                continue

            if ".method public final isFree(" in line:
                output.append(line)
                output.append(textwrap.indent(textwrap.dedent("""\
                        .locals 1

                        const/4 v0, 0x0
                        return v0
                    """), "\t"))
                skip = True
                continue

            if ".method public final isPremium(" in line:
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

Claim("pt.tscg.mtgmanager/smali_classes6/com/bigar/manager/business/model/Claim.smali")
LicenseClient("pt.tscg.mtgmanager/smali_classes2/com/pairip/licensecheck/LicenseClient.smali")
ManagerPreferencesHelper("pt.tscg.mtgmanager/smali_classes6/com/bigar/manager/helper/ManagerPreferencesHelper.smali")
SubscriptionHelper("pt.tscg.mtgmanager/smali_classes6/com/bigar/manager/helper/SubscriptionHelper.smali")