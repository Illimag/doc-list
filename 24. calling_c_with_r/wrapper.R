# Wrapper function to invoke "helloA" at the shell.
helloA <- function() {
  system(paste(getwd(),"helloA",sep="/"))
}