library(maps)
library(geosphere)

map("state")
flights = read.csv("C:\\Users\\563572\\Documents\\Python Scripts\\aggregate_DC.csv")

#flights$delay = ifelse(flights$DEST=="DCA",flights$ARR_DELAY,flights$ARR_DELAY)
library(Hmisc)
flightsOut = flights[flights$Direction == "Out",]
flightsOut$delay_bucket = as.numeric(cut2(flightsOut[flightsOut$Direction=="Out",]$ARR_DELAY, g=10))
c= rainbow(10, start=0, end=2/3)
map("world", col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05, xlim=xlim, ylim=ylim)

for(i in 1:10){
  fsub = flightsOut[flightsOut$delay_bucket ==i ,]#%in% levels(flights$CARRIER)[i],]
  #fsub = flights
  for (j in 1:length(fsub$CARRIER)) {
    #air1 <- airports[airports$iata == fsub[j,]$airport1,]
    #air2 <- airports[airports$iata == fsub[j,]$airport2,]
    #inter <- gcIntermediate(c(air1[1,]$long, air1[1,]$lat), c(air2[1,]$long, air2[1,]$lat), n=100, addStartEnd=TRUE)
    
    inter <- gcIntermediate(c(fsub[j,]$ORIGIN_long, fsub[j,]$ORIGIN_lat),c(fsub[j,]$DEST_long, fsub[j,]$DEST_lat), n=100, addStartEnd=TRUE)
    
    lines(inter, col=c[i], lwd=0.8)
  }
}
legend(-70,50, # places a legend at the appropriate place 
       round(aggregate(ARR_DELAY ~ delay_bucket, data=flightsOut, "mean")$ARR_DELAY,0), # puts text in the legend 
       lty=c(1,1), # gives the legend appropriate symbols (lines)
       col=c) # gives the legend lines the correct color and width

map("world", col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05, xlim=xlim, ylim=ylim)
flightsIn = flights[flights$Direction == "Into",]
flightsIn$delay_bucket = as.numeric(cut2(flightsIn$ARR_DELAY, g=10))
for(i in 1:10){
  fsub = flightsIn[flightsIn$delay_bucket ==i,]#%in% levels(flights$CARRIER)[i],]
  #fsub = flights
  for (j in 1:length(fsub$CARRIER)) {
    #air1 <- airports[airports$iata == fsub[j,]$airport1,]
    #air2 <- airports[airports$iata == fsub[j,]$airport2,]
    #inter <- gcIntermediate(c(air1[1,]$long, air1[1,]$lat), c(air2[1,]$long, air2[1,]$lat), n=100, addStartEnd=TRUE)
    
    inter <- gcIntermediate(c(fsub[j,]$ORIGIN_long, fsub[j,]$ORIGIN_lat),c(fsub[j,]$DEST_long, fsub[j,]$DEST_lat), n=100, addStartEnd=TRUE)
    
    lines(inter, col=c[i], lwd=0.8)
  }
}
legend(-70,50, # places a legend at the appropriate place 
       round(aggregate(ARR_DELAY ~ delay_bucket, data=flightsIn, "mean")$ARR_DELAY,0), # puts text in the legend 
       lty=c(1,1), # gives the legend appropriate symbols (lines)
       col=c) # gives the legend lines the correct color and width

map("world", col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05, xlim=xlim, ylim=ylim)
c = rainbow(13)
for(i in 1:13){
  fsub = flights[flights$CARRIER %in% levels(flights$CARRIER)[i],]
  #fsub = flights
  for (j in 1:length(fsub$CARRIER)) {
    #air1 <- airports[airports$iata == fsub[j,]$airport1,]
    #air2 <- airports[airports$iata == fsub[j,]$airport2,]
    #inter <- gcIntermediate(c(air1[1,]$long, air1[1,]$lat), c(air2[1,]$long, air2[1,]$lat), n=100, addStartEnd=TRUE)
    
    inter <- gcIntermediate(c(fsub[j,]$ORIGIN_long, fsub[j,]$ORIGIN_lat),c(fsub[j,]$DEST_long, fsub[j,]$DEST_lat), n=100, addStartEnd=TRUE)
    
    lines(inter, col=c[i], lwd=0.8)
  }
}
legend(-70,50, # places a legend at the appropriate place 
       levels(flights$CARRIER), # puts text in the legend 
       lty=c(1,1), # gives the legend appropriate symbols (lines)
       col=c) # gives the legend lines the correct color and width


night_loops = read.csv("C:\\Users\\563572\\Documents\\Python Scripts\\night_loop.csv")
map("world", col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05, xlim=xlim, ylim=ylim)

night_loops = subset(night_loops, ARR_DELAY>250 & FREQ > 1)
night_loops = droplevels(night_loops)
c = rainbow(length(levels(night_loops$CARRIER)))
for(i in 1:length(levels(night_loops$CARRIER))){
  fsub = night_loops[night_loops$CARRIER %in% levels(night_loops$CARRIER)[i],]
  #fsub = night_loops
  for (j in 1:length(fsub$CARRIER)) {
    #air1 <- airports[airports$iata == fsub[j,]$airport1,]
    #air2 <- airports[airports$iata == fsub[j,]$airport2,]
    #inter <- gcIntermediate(c(air1[1,]$long, air1[1,]$lat), c(air2[1,]$long, air2[1,]$lat), n=100, addStartEnd=TRUE)
    
    inter <- gcIntermediate(c(fsub[j,]$longitude_x, fsub[j,]$latitude_x),c(fsub[j,]$longitude_y, fsub[j,]$latitude_y), n=100, addStartEnd=TRUE)
    
    lines(inter, col=c[i], lwd=0.8)
  }
}
legend(-65,50, # places a legend at the appropriate place 
       levels(night_loops$CARRIER), # puts text in the legend 
       lty=c(1,1), # gives the legend appropriate symbols (lines)
       col=c) # gives the legend lines the correct color and width



