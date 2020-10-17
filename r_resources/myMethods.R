setPath <- function(){
  #Seteamos el directorio principal
  setwd("D:/Workspaces/eclipse-workspace/TFG/RecommenderSystem/r_resources")
  setwd("~/GitHub/RecommenderSystem/r_resources")
  getwd()
}

updateLibrarys <- function(){
  
  install.packages("installr", dependencies = TRUE)
  library(installr)
  updateR()
  
}

importLibrarys <- function(){
  library(cluster)
  library(ggplot2)
  library(pheatmap)
  library(caret)
  library(lattice)
  library(factoextra)
  library(MASS)
  library(dplyr)
  library(corrplot)   #Para pintar matriz de correlacion
}


preprocesarDataFrame<- function(df,estandarizar=FALSE){
  #Quitamos NA y ponemos 0
  print("#Quitamos NA y ponemos 0")
  df[is.na(df)] <- 0
  #Quitar filas que sumen 0
  print("#Quitar filas que sumen 0")
  df=df[which(rowSums(df)!=0),]
  #Quitar columnas que sumen 0
  print("#Quitar columnas que sumen 0")
  df=df[, which(colSums(df)!=0)]
  if(estandarizar){
    ##Estandarizacion
    #Center TRUE resta la media - Scale TRUE divide por des. tip.
    print("##Estandarizacion")
    df<-scale(df, center = TRUE, scale = TRUE)
    #Pasamos a dataFrame
    print("#Pasamos a dataFrame")
    df<-as.data.frame(df)
  }
  return (df)
}
















