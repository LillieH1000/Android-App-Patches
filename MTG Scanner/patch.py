import textwrap

# Claim (smali_classes6)

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

# LicenseClient (smali_classes2)

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

# ManagerPreferencesHelper (smali_classes6)

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

# SubscriptionHelper (smali_classes6)

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

# Patches

Claim("pt.tscg.mtgmanager/smali_classes6/com/bigar/manager/business/model/Claim.smali") # Premium Banners
LicenseClient("pt.tscg.mtgmanager/smali_classes2/com/pairip/licensecheck/LicenseClient.smali") # Play Store Check
ManagerPreferencesHelper("pt.tscg.mtgmanager/smali_classes6/com/bigar/manager/helper/ManagerPreferencesHelper.smali") # Premium Popups
SubscriptionHelper("pt.tscg.mtgmanager/smali_classes6/com/bigar/manager/helper/SubscriptionHelper.smali") # Premium Check - Free Check - Premium Popups