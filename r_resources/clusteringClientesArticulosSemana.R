#Seteamos el directorio principal
setwd("D:/Workspaces/eclipse-workspace/TFG/RecommenderSystem/r_resources")
setwd("~/GitHub/RecommenderSystem/r_resources")
getwd()

install.packages("installr", dependencies = TRUE)
library(installr)
updateR()

#Cargamos las librerias
install.packages(c("mlbench","cluster","latice","factoextra","biclust","caret","pheatmap"))
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
dataClienteArticuloSemana <- read.csv("../files/similarityMatrix/dataClienteArticuloSimple.csv", row.names=1, na.strings="0",check.names=FALSE)
#a1,a2,a3,a4,a5
#Copiamos los datos
clienteCompraPrep=dataClienteArticuloSemana[,]
#Summary
#summary(clienteCompra)

####  Preprocesamiento  ####

#Quitamos NA y ponemos 0
clienteCompraPrep[is.na(clienteCompraPrep)] <- 0
#Quitar filas que sumen 0
clienteCompraPrep=clienteCompraPrep[which(rowSums(clienteCompraPrep)!=0),]
#Quitar columnas que sumen 0
clienteCompraPrep=clienteCompraPrep[, which(colSums(clienteCompraPrep)!=0)]
##Estandarizacion
#Center TRUE resta la media - Scale TRUE divide por des. tip.
clienteCompraPrep<-scale(clienteCompraPrep, center = TRUE, scale = TRUE)
#Pasamos a dataFrame
clienteCompraPrep<-as.data.frame(clienteCompraPrep)
#### Clustering ####

#Muestreo Aleatorio
muestreo <- sample_n(clienteCompraPrep, size= 250)
#Determinar numero de clusters en base al muestreo
fviz_nbclust(muestreo, kmeans,method = "gap_stat")

#Seteamos la semilla
set.seed(1996) # para reproducibilidad
numCluster=10
clusters.km <- kmeans(clienteCompraPrep,numCluster,nstart = 25)
clusters.km$size
data_clus_1 <- clienteCompraPrep[clusters.km$cluster == 1,]
data_clus_2 <- clienteCompraPrep[clusters.km$cluster == 2,]
data_clus_3 <- clienteCompraPrep[clusters.km$cluster == 3,]



fviz_cluster(clusters.km, data = clienteCompraPrep, palette = "jco", ggtheme = theme_minimal())


##### Sacar CSV con los id de usuarios por cluster #####

for (i in 1:numCluster) {
  nombreFile=paste(paste("../files/clusters/CPSclus_Scale_03Octubre_",sep="",i),sep="",".csv")
  write.csv(clienteCompraPrep[clusters.km$cluster == i,], file=nombreFile)
}
#####   Matrices de correlacion   #####
for (i in 1:2) {
  #cluster=paste(paste("data_clus_Gasto",sep="",i),sep="",".png")
  #dev=png(cluster) 
  distance <- get_dist(clienteCompraPrep[clusters.km$cluster == 3,])
  fviz_dist(distance, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))
  ##  Close the file
  #dev.off() 
  
}


print("finish")

