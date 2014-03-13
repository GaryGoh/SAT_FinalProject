__author__ = 'GaryGoh'

## To generate the cnf file header
def write_header(variables, clauses, fileName):
    cnfFile = open(str(fileName), "w")

    header = "p cnf " + str(variables) + " " + str(clauses)
    cnfFile.write(header + "\n")

## To write the clauses to CNF file
# def write_clauses(variables, clauses, fileName):
#     cnfFile = open(str(fileName), "a")
#     header = "p cnf " + str(variables) + " " + str(clauses)
#     cnfFile.write(header + "\n")
#
#     cnfFile.close()
#     return


# write_header(2, 6, "test.cnf")


