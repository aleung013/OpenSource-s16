library(arules)
library(arulesViz)

str(admissions)
col_names <- names(admissions)
admissions[,col_names] <- lapply(admissions[,col_names],factor)


rules.all <- eclat(admissions)
inspect(rules.all)
plot(rules.all)

rules.all <- apriori(admissions,
                     parameter = list(minlen=1,supp=0.01,conf=0.2),
                     appearance = list(rhs=c("admit=1"),lhs=c("rank=1")))
inspect(rules.all)
plot(rules.all)

plot(rules.all,method="grouped")

plot(rules.all,method="graph")

plot(rules.all,method="graph",control=list(type="items"))

plot(rules.all, method="paracoord",control=list(reorder=TRUE))

rules.all <- apriori(admissions,
                     parameter = list(minlen=1,supp=0.03,conf=0.5),
                     appearance = list(rhs=c("admit=0"),lhs=c("rank=1")))
inspect(rules.all)
plot(rules.all)