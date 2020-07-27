import os
import reformat

CWD = os.getcwd()


def group_headers_indicators(source):
    """
    Groups indicators according to corresponding headers.
    :param source: folder in which data is located
    :return: None
    """
    with open(os.path.join(CWD, source, "headers-lvl1.txt"), 'r') as f:
        h1_list = [row.replace("\n", "") for row in f]
    with open(os.path.join(CWD, source, "headers-lvl2.txt"), 'r') as f:
        h2_list = [row.replace("\n", "") for row in f]
    with open(os.path.join(CWD, source, "headers-lvl3.txt"), 'r') as f:
        h3_list = [row.replace("\n", "") for row in f]
    with open ("{}_results.txt".format(source), "w", encoding="utf8") as output:
        output.write("|".join(("h1", "h2", "h3", "ind", "\n")))
        with open(os.path.join(CWD, source, "ind_headers123.txt"), "r") as source_file:
            h1 = h2 = h3 = ind = "-"
            for row in source_file:
                row = row.replace("\n", "")
                if not row:
                    pass
                elif row in h1_list:
                    h1 = row
                    h3 = h2 = "-"
                elif row in h2_list:
                    h2 = row
                    h3 = "-"
                elif row in h3_list:
                    h3 = row
                else:
                    ind = row
                    output.write("|".join(('"' + h1 + '"', '"' + h2 + '"', '"' + h3 + '"', '"' + ind + '"', "\n")))
    return


if __name__ == '__main__':
    reformat.reformat()
    for source in ("data_basque", "data_spanish"):
        group_headers_indicators(source)
