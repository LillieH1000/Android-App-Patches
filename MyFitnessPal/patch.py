import textwrap

# HeaderUI (smali_classes16)

def HeaderUI(path):
    with open(path, "r") as file:
        lines = file.readlines()

        output = []
        method = False
        skip = False

        for line in lines:
            if ".method public final component1(" in line or ".method public final component2(" in line:
                method = True
                output.append(line)
                continue

            if method:
                if ".locals 0" in line:
                    output.append(line)
                    output.append(textwrap.indent(textwrap.dedent("""
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
            else:
                output.append(line)

    with open(path, "w") as file:
        file.writelines(output)

# SubscriptionStateKt (smali_classes6)

def SubscriptionStateKt(path):
    with open(path, "r") as file:
        lines = file.readlines()

        output = []
        method = False
        skip = False

        for line in lines:
            if ".method public static final isPremium(" in line or ".method public static final isPremiumPlus(" in line or ".method public static final isSubscribed(" in line:
                method = True
                output.append(line)
                continue

            if method:
                if "invoke-static" in line and "checkNotNullParameter" in line:
                    output.append(line)
                    output.append(textwrap.indent(textwrap.dedent("""
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
            else:
                output.append(line)

    with open(path, "w") as file:
        file.writelines(output)

# Patches

HeaderUI("com.myfitnesspal.android/smali_classes16/com/myfitnesspal/dashboard/model/HeaderUI$Loaded.smali")
SubscriptionStateKt("com.myfitnesspal.android/smali_classes6/com/myfitnesspal/service/premium/subscription/data/repository/SubscriptionStateKt.smali")