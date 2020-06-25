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

require(ppclust)
require(fclust)
#Leemos los datos
dataClienteFamilia <- read.csv("../files/similarityMatrix/dataGastoClienteFamilia.csv", row.names=1, na.strings="0")

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
#Clustering Difuso
numCluster=5
#fanny(clientefamPrep, numCluster, metric = "euclidean", stand = FALSE) Es CMEANS? Preguntar MIGUEL
res.fcm <- fcm(clientefamPrep, centers=5)
summary(res.fcm)
plotcluster(res.fcm, cp=1, trans=TRUE)


fviz_cluster(clusters.km, data = clientefamPrep, palette = "jco", ggtheme = theme_minimal())

res.fcm3 <- ppclust2(res.fcm, "fanny")
cluster::clusplot(scale(clientefamPrep), res.fcm3$cluster,  
                  main = "Cluster plot of Iris data set",
                  color=TRUE, labels = 2, lines = 2, cex=1)








##### Sacar CSV con los id de usuarios por cluster #####

for (i in 1:numCluster) {
  nombreFile=paste(paste("../files/clusters/clusGasto",sep="",i),sep="",".csv")
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

setwd("D:/Workspaces/eclipse-workspace/TFG/RecommenderSystem/r_resources")
#getwd()
