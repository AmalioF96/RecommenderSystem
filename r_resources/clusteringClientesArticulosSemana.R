#Seteamos el directorio principal
setwd("D:/Workspaces/eclipse-workspace/TFG/RecommenderSystem/r_resources")
getwd()

#Cargamos las librerias
library(cluster)
library(ggplot2)
library(pheatmap)
library(caret)
library(lattice)
library(factoextra)
library(MASS)
library(dplyr)
library(corrplot)   #Para pintar matriz de correlacion

#Leemos los datos
dataClienteFamilia <- read.csv("D:/Workspaces/eclipse-workspace/TFG/RecommenderSystem/files/similarityMatrix/dataClienteArticuloSimple.csv", row.names=1, na.strings="0")

#Copiamos los datos
clientefam=dataClienteFamilia[,]
#Summary
#summary(clientefam)

####  Preprocesamiento  ####

#Quitamos NA y ponemos 0
clientefam[is.na(clientefam)] <- 0
#Quitar filas que sumen 0
clientefamPrep=clientefam[which(rowSums(clientefam)!=0),]
#Quitar columnas que sumen 0
clientefamPrep=clientefamPrep[, which(colSums(clientefamPrep)!=0)]
##Estandarizacion
#Center TRUE resta la media - Scale TRUE divide por des. tip.
clientefamPrep<-scale(clientefamPrep, center = TRUE, scale = TRUE)
#Pasamos a dataFrame
clientefamPrep<-as.data.frame(clientefamPrep)
#### Clustering ####

#Muestreo Aleatorio
muestreo <- sample_n(clientefamPrep, size= 250)
#Determinar numero de clusters en base al muestreo
fviz_nbclust(muestreo, kmeans,method = "gap_stat")

#Seteamos la semilla
set.seed(1996) # para reproducibilidad
numCluster=5
clusters.km <- kmeans(clientefamPrep,numCluster,nstart = 25)
clusters.km$size
data_clus_1 <- clientefamPrep[clusters.km$cluster == 1,]
data_clus_2 <- clientefamPrep[clusters.km$cluster == 2,]
data_clus_3 <- clientefamPrep[clusters.km$cluster == 3,]



fviz_cluster(clusters.km, data = clientefamPrep, palette = "jco", ggtheme = theme_minimal())


##### Sacar CSV con los id de usuarios por cluster #####

for (i in 1:numCluster) {
  nombreFile=paste(paste("../files/clusters/CPSclus",sep="",i),sep="",".csv")
  write.csv(clientefamPrep[clusters.km$cluster == i,], file=nombreFile)
}
#####   Matrices de correlacion   #####
for (i in 1:2) {
  #cluster=paste(paste("data_clus_Gasto",sep="",i),sep="",".png")
  #dev=png(cluster) 
  distance <- get_dist(clientefamPrep[clusters.km$cluster == 3,])
  fviz_dist(distance, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
  ##  Close the file
  #dev.off() 
  
}


print("finish")

