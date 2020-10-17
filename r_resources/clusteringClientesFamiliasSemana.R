source("myMethods.R")
setPath()
updateLibrarys()
importLibrarys()


#Leemos los datos
dataframe <- read.csv("../files/similarityMatrix/dataClienteFamiliaSimple.csv", row.names=1, na.strings="0",check.names=FALSE)

#Copiamos los datos
dfCopy=dataframe[,]
#Summary
#summary(dfCopy)

####  Preprocesamiento  ####
dfCopy <-preprocesarDataFrame(dfCopy)

#### Clustering ####

#Muestreo Aleatorio
muestreo <- sample_n(dfCopy, size= 800)
#Determinar numero de clusters en base al muestreo
fviz_nbclust(muestreo, kmeans,method = "gap_stat")

#Seteamos la semilla
set.seed(1996) # para reproducibilidad
numCluster=5
clusters.km <- kmeans(dfCopy,numCluster,nstart = 25)
clusters.km$size
data_clus_1 <- dfCopy[clusters.km$cluster == 1,]
data_clus_2 <- dfCopy[clusters.km$cluster == 2,]
data_clus_3 <- dfCopy[clusters.km$cluster == 3,]
data_clus_3 <- dfCopy[clusters.km$cluster == 4,]
data_clus_3 <- dfCopy[clusters.km$cluster == 5,]



fviz_cluster(clusters.km, data = dfCopy, palette = "jco", ggtheme = theme_minimal())
##### Sacar CSV con los id de usuarios por cluster #####

for (i in 1:numCluster) {
  nombreFile=paste(paste("../files/clusters/clusters17Octubre/ClientesFamilias_clus_",sep="",i),sep="",".csv")
  write.csv(dfCopy[clusters.km$cluster == i,], file=nombreFile)
}

distance <- get_dist(dfCopy[clusters.km$cluster == 3,])
fviz_dist(distance, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
