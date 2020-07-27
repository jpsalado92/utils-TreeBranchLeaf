import os

CWD = os.getcwd()


def reformat():
    """
    Reformat raw and redundant data to a standard.
    :return: None
    """
    for folder, title in (("data_basque", "IZENBURUAK"), ("data_spanish", "TITULOS")):
        current_path = os.path.join(CWD, folder)

        f1_headers = []
        with open(os.path.join(current_path, "{}1.txt".format(title)), "r", encoding="utf8") as f1:
            with open(os.path.join(current_path, "headers-lvl1.txt"), "w") as f1n:
                for row in f1:
                    if not row or row == " " or row == "\n":
                        pass
                    else:
                        f1_headers.append(row)
                        f1n.write(row)

        f2_headers = []
        with open(os.path.join(current_path, "{}1+2.txt".format(title)), "r", encoding="utf8") as f12:
            with open(os.path.join(current_path, "headers-lvl2.txt"), "w") as f2:
                for row in f12:
                    if row in f1_headers or row == " " or row == "\n":
                        pass
                    else:
                        f2_headers.append(row)
                        f2.write(row)

        with open(os.path.join(current_path, "{}1+2+3.txt".format(title)), "r", encoding="utf8") as f123:
            with open(os.path.join(current_path, "headers-lvl3.txt"), "w") as f3:
                for row in f123:
                    if any(row in head_f for head_f in (f1_headers, f2_headers)) or (not row) or (row == " ") or (
                            row == "\n"):
                        pass
                    else:
                        f3.write(row)

        with open(os.path.join(current_path, "{}1+2+3+IND.txt".format(title)), "r", encoding="utf8") as f123h:
            with open(os.path.join(current_path, "ind_headers123.txt"), "w") as f123hn:
                for row in f123h:
                    if not row or (row == " ") or (row == "\n"):
                        pass
                    else:
                        f123hn.write(row)
    return


if __name__ == '__main__':
    reformat()
