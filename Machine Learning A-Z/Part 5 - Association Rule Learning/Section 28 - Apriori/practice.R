# Apriori

# Data Processing 
library(arules)
dataset = read.csv('Market_Basket_Optimisation.csv', header=FALSE)
dataset = read.transactions('Market_Basket_Optimisation.csv', 
                            sep = ',',
                            rm.duplicates = TRUE
                            )
summary(dataset)
itemFrequencyPlot(dataset, topN = 100)

# Training Apriori on the dataset
rules = apriori(dataset,
                parameter = list(support = 0.003, confidence = 0.4))

